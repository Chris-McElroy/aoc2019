//
//  helpers.swift
//  aoc2019
//
//  Created by Chris McElroy on 11/16/21.
//

import Foundation
import Accelerate
import CryptoKit

// input functions //

public func inputStrings(_ separator: String = "\n") -> [String] {
	do {
		let home = FileManager.default.homeDirectoryForCurrentUser
		let name = "input" + (day < 10 ? "0" : "") + "\(day)"
		let filePath = projectFolder + "/aoc2019/" + name
		let file = URL(fileURLWithPath: filePath, relativeTo: home)
		let list = try String(contentsOf: file).dropLast().components(separatedBy: separator)
		return list
	} catch {
		print("Error: bad file name")
		return []
	}
}

public func inputInts(_ separator: String = "\n") -> [Int] {
	let input = inputStrings(separator)
	return input.compactMap { Int($0) ?? nil }
}

public func inputWords(_ wordSeparators: [String] = [" "], _ lineSeparator: String = "\n") -> [[String]] {
	var words = inputStrings(lineSeparator).map { [$0] }
	for wordSeparator in wordSeparators {
		words = words.map { line in line.flatMap { $0.components(separatedBy: wordSeparator) } }
	}
	words = words.map { line in line.filter { $0 != "" } }
	return words
}

public func inputIntWords(_ wordSeparators: [String] = [" "], _ lineSeparator: String = "\n") -> [[Int]] {
	let input = inputWords(wordSeparators, lineSeparator)
	return input.map { words in words.map { word in Int(word)! } }
}

public func inputSomeInts(words: [Int], _ wordSeparators: [String] = [" "], _ lineSeparator: String = "\n") -> [[Int]] {
	let input = inputWords(wordSeparators, lineSeparator)
	return words.map { word in input.map { line in Int(line[word])! } }
}

//public func inputAllInts() -> [[Int]] {
//	let input = inputStrings()
//	var output: [[Int]] = []
//	var currentInt: String = ""
//	for line in input {
//		var lineInts: [Int] = []
//		for c in line {
//			if c.isNumber || (c == "-" && currentInt == "") {
//				currentInt.append(c)
//			} else if currentInt != "" {
//				lineInts.append(Int(currentInt)!)
//				currentInt = ""
//			}
//		}
//		output.append(lineInts)
//	}
//	return output
//}

public func inputOneInt(word: Int, _ wordSeparators: [String] = [" "], _ lineSeparator: String = "\n") -> [Int] {
	let input = inputWords(wordSeparators, lineSeparator)
	return input.map { line in Int(line[word])! }
}

// shortcuts //

func make2DArray<Element>(repeating repeatedValue: Element, count1: Int, count2: Int) -> [[Element]] {
	(0..<count1).map { _ in Array(repeating: repeatedValue, count: count2) }
}

public extension Collection where Indices.Iterator.Element == Index {
	func first(_ k: Int) -> SubSequence {
		return self.dropLast(count-k)
	}
	
	func last(_ k: Int) -> SubSequence {
		return self.dropFirst(count-k)
	}
	
	subscript(r: Range<Int>) -> SubSequence {
		get {
			self.first(r.upperBound).dropFirst(r.lowerBound)
		}
	}
	
	subscript(r: ClosedRange<Int>) -> SubSequence {
		get {
			self[r.lowerBound..<(r.upperBound + 1)]
		}
	}
	
	func each(_ k: Int) -> Array<SubSequence> {
		var array: Array<SubSequence> = []
		var i = 0
		while i < count {
			array.append(self[i..<(Swift.min(i + k, count))])
			i += k
		}
		return array
	}
	
	// from https://stackoverflow.com/a/54350570
	func toTuple() -> (Element) {
		return (self[0 as! Self.Index])
	}
	
	func toTuple() -> (Element, Element) {
		return (self[0 as! Self.Index], self[1 as! Self.Index])
	}
	
	func toTuple() -> (Element, Element, Element) {
		return (self[0 as! Self.Index], self[1 as! Self.Index], self[2 as! Self.Index])
	}
	
	func toTuple() -> (Element, Element, Element, Element) {
		return (self[0 as! Self.Index], self[1 as! Self.Index], self[2 as! Self.Index], self[3 as! Self.Index])
	}
	
	func toTuple() -> (Element, Element, Element, Element, Element) {
		return (self[0 as! Self.Index], self[1 as! Self.Index], self[2 as! Self.Index], self[3 as! Self.Index], self[4 as! Self.Index])
	}
}

public extension Collection where Element: Equatable {
	func repeats(of e: Element) -> Int {
		return self.filter({ $0 == e }).count
	}
}

public extension Collection where Element: Hashable {
	func occurs(min: Int) -> Array<Element> {
		var counts: Dictionary<Element, Int> = [:]
		self.forEach { counts[$0, default: 0] += 1 }
		return Array(counts.filter { $0.value >= min }.keys)
	}
}

public extension Collection where Element: Numeric {
	func product() -> Element {
		return self.reduce(1) { x,y in x*y }
	}
	
	func sum() -> Element {
		return self.reduce(0) { x,y in x+y }
	}
}

public extension Collection where Element: AdditiveArithmetic {
	func twoSumTo(_ s: Element) -> [Element]? {
		guard let x = first(where: { contains(s-$0) }) else { return nil }
		return [x, s-x]
	}
	
	func nSumTo(_ s: Element, n: Int) -> [Element]? {
		if n == 2 { return twoSumTo(s) }
		for e in self {
			if var arr = nSumTo(s-e, n: n-1) {
				arr.append(e)
				return arr
			}
		}
		return nil
	}
}

public extension Array {
	subscript(w i: Int) -> Iterator.Element? {
		return self[index(startIndex, offsetBy: i % count)]
	}
	
	subscript(guarded i: Int) -> Iterator.Element? {
		if i < 0 || i >= count { return nil }
		return self[i]
	}
	
	func first(_ k: Int) -> Self.SubSequence {
		return self.dropLast(count-k)
	}
	
	func last(_ k: Int) -> Self.SubSequence {
		return self.dropFirst(count-k)
	}
	
	subscript(r: Range<Int>) -> Self.SubSequence {
		get {
			self.first(r.upperBound).dropFirst(r.lowerBound)
		}
		set {
			let start = index(startIndex, offsetBy: r.lowerBound)
			let end = index(startIndex, offsetBy: r.upperBound)
			replaceSubrange(start..<end, with: newValue)
		}
	}
	
	subscript(r: ClosedRange<Int>) -> Self.SubSequence {
		get {
			self[r.lowerBound..<(r.upperBound + 1)]
		}
		set {
			self[r.lowerBound..<(r.upperBound + 1)] = newValue
		}
	}
	
	subscript(r: Range<Int>, by k: Int) -> Self {
		get {
			self[r].enumerated().compactMap { i,e in i.isMultiple(of: k) ? e : nil }
		}
		set {
			var i = r.lowerBound
			for element in newValue {
				if i >= r.upperBound { break }
				self[i] = element
				i += k
			}
		}
	}
	
	subscript(r: ClosedRange<Int>, by k: Int) -> Self {
		get {
			self[r.lowerBound..<(r.upperBound + 1), by: k]
		}
		set {
			self[r.lowerBound..<(r.upperBound + 1), by: k] = newValue
		}
	}
	
	subscript(_ s: Int, _ e: Int) -> Self.SubSequence {
		return self.first(e).dropFirst(s)
	}
	
	mutating func pushOn(_ new: Element) {
		self = self.dropFirst() + [new]
	}
}

public extension Array where Element: Equatable {
	func fullSplit(separator: Element) -> Array<Self> {
		return self.split(whereSeparator: { $0 == separator}).map { Self($0) }
	}
}

public extension Dictionary {
	init<Element>(from array: [[Element]], key: Int, value: Int) where Element: Hashable {
		self.init()
		for part in array {
			self[part[key] as! Key] = part[value] as? Value
		}
	}
	
	init<Element>(from array: [[Element]], key: Int) where Value == [Element], Element: Hashable {
		self.init()
		for part in array {
			self[part[key] as! Key] = part
		}
	}
}

public extension String {
//	func fullSplit(separator: Character) -> [String] {
//		let s = self.split(separator: separator, maxSplits: .max, omittingEmptySubsequences: false).map { String($0) }
//		if s.last == "" {
//			return s.dropLast(1)
//		} else {
//			return s
//		}
//	}
	
	func occurs(min: Int) -> String {
		var counts: Dictionary<Character, Int> = [:]
		self.forEach { counts[$0, default: 0] += 1 }
		return String(counts.filter { $0.value >= min }.keys)
	}
	
	subscript(i: Int) -> Character {
		get {
			self[index(startIndex, offsetBy: i)]
		}
		set {
			let index = index(startIndex, offsetBy: i)
			replaceSubrange(index...index, with: String(newValue))
		}
	}
	
	subscript(w i: Int) -> Character? {
		return self[index(startIndex, offsetBy: i % count)]
	}
	
	subscript(s i: Int) -> Character? {
		if i < 0 || i >= count { return nil }
		return self[i]
	}
	
	subscript(r: Range<Int>) -> String {
		get {
			String(self.first(r.upperBound).dropFirst(r.lowerBound))
		}
		set {
			let start = index(startIndex, offsetBy: r.lowerBound)
			let end = index(startIndex, offsetBy: r.upperBound)
			replaceSubrange(start..<end, with: newValue)
		}
	}
	
	subscript(r: ClosedRange<Int>) -> String {
		get {
			self[r.lowerBound..<(r.upperBound + 1)]
		}
		set {
			self[r.lowerBound..<(r.upperBound + 1)] = newValue
		}
	}
	
	subscript(r: Range<Int>, by k: Int) -> String {
		get {
			return String(self[r].enumerated().compactMap { i,e in i.isMultiple(of: k) ? e : nil })
		}
		set {
			var i = r.lowerBound
			for element in newValue {
				if i >= r.upperBound { break }
				self[i] = element
				i += k
			}
		}
	}
	
	subscript(r: ClosedRange<Int>, by k: Int) -> String {
		get {
			self[r.lowerBound..<(r.upperBound + 1), by: k]
		}
		set {
			self[r.lowerBound..<(r.upperBound + 1), by: k] = newValue
		}
	}
	
	func firstIndex(of element: Character) -> Int? {
		firstIndex(of: element)?.utf16Offset(in: self)
	}
	
	func lastIndex(of element: Character) -> Int? {
		lastIndex(of: element)?.utf16Offset(in: self)
	}
}

public extension StringProtocol {
	subscript(offset: Int) -> Character {
		self[index(startIndex, offsetBy: offset)]
	}
	
	subscript(_ s: Int, _ e: Int) -> SubSequence {
		return self.first(e).dropFirst(s)
	}
	
	func first(_ k: Int) -> Self.SubSequence {
		return self.dropLast(count-k)
	}
	
	func last(_ k: Int) -> Self.SubSequence {
		return self.dropFirst(count-k)
	}
	
	subscript(r: Range<Int>) -> String {
		get {
			String(self.first(r.lowerBound).dropFirst(r.upperBound))
		}
	}
	
	subscript(r: ClosedRange<Int>) -> String {
		get {
			self[r.lowerBound..<(r.upperBound + 1)]
		}
	}
	
	subscript(r: Range<Int>, by k: Int) -> String {
		get {
			return String(self[r].enumerated().compactMap { i,e in i.isMultiple(of: k) ? e : nil })
		}
	}
	
	subscript(r: ClosedRange<Int>, by k: Int) -> String {
		get {
			self[r.lowerBound..<(r.upperBound + 1), by: k]
		}
	}
	
	func isin(_ string: Self?) -> Bool {
		return string?.contains(self) == true
	}
	
	func repititions(n: Int) -> [Character] {
		var last: Character = " "
		var count = 0
		var output: [Character] = []
		
		for c in self {
			if last == c {
				count += 1
				if count == n {
					output.append(c)
				}
			} else {
				last = c
				count = 1
			}
		}
		
		return output
	}
}

public extension Character {
	static func +(lhs: Character, rhs: Int) -> Character {
		if lhs.isLetter {
			let aVal: UInt32 = lhs.isUppercase ? 65 : 97
			if let value = lhs.unicodeScalars.first?.value {
				if let scalar = UnicodeScalar((value - aVal + UInt32(rhs)) % 26 + aVal) {
					return Character(scalar)
				}
			}
		}
		return lhs
	}
}

extension RangeReplaceableCollection {
	// from https://stackoverflow.com/questions/25162500/apple-swift-generate-combinations-with-repetition
	// I should use rangereplacablecollection for everything i think
	func combinations(of n: Int) -> [SubSequence] {
		guard n > 0 else { return [.init()] }
		guard let first = first else { return [] }
		return combinations(of: n - 1).map { CollectionOfOne(first) + $0 } + dropFirst().combinations(of: n)
	}
	func uniqueCombinations(of n: Int) -> [SubSequence] {
		guard n > 0 else { return [.init()] }
		guard let first = first else { return [] }
		return dropFirst().uniqueCombinations(of: n - 1).map { CollectionOfOne(first) + $0 } + dropFirst().uniqueCombinations(of: n)
	}
	
	mutating func insert(_ newElement: Self.Element, _ i: Int) {
		self.insert(newElement, at: index(self.startIndex, offsetBy: i))
	}
}

// permutations from https://stackoverflow.com/questions/34968470/calculate-all-permutations-of-a-string-in-swift
func permutations<T>(len n: Int, _ a: inout [T], output: inout [[T]]) {
	if n == 1 { output.append(a); return }
	for i in stride(from: 0, to: n, by: 1) {
		permutations(len: n-1, &a, output: &output)
		a.swapAt(n-1, (n%2 == 1) ? 0 : i)
	}
}

public extension Comparable {
	func isin(_ collection: Array<Self>?) -> Bool {
		return collection?.contains(self) == true
	}
	
	mutating func swap(_ x: Self, _ y: Self) {
		self = (self == x) ? y : x
	}
}

public extension Equatable {
	func isin(_ one: Self, _ two: Self, _ three: Self) -> Bool {
		return self == one || self == two || self == three
	}
}

public extension Hashable {
	func isin(_ collection: Set<Self>?) -> Bool {
		return collection?.contains(self) == true
	}
}

public extension Character {
	func isin(_ string: String?) -> Bool {
		return string?.contains(self) == true
	}
}

public extension Numeric where Self: Comparable {
	func isin(_ range: ClosedRange<Self>?) -> Bool {
		return range?.contains(self) == true
	}
	
	func isin(_ range: Range<Self>?) -> Bool {
		return range?.contains(self) == true
	}
}

infix operator ** : MultiplicationPrecedence
public extension Numeric {
	func sqrd() -> Self {
		self*self
	}
	
	static func ** (lhs: Self, rhs: Int) -> Self {
		(0..<rhs).reduce(1) { x,y in x*lhs }
	}
}

public extension Bool {
	var int: Int { self ? 1 : 0 }
}

func timed(_ run: () -> Void) {
	let start = Date().timeIntervalSinceReferenceDate
	run()
	let end = Date().timeIntervalSinceReferenceDate
	print("in:", end-start)
}

public extension BinaryFloatingPoint {
	var isWhole: Bool { self.truncatingRemainder(dividingBy: 1) == 0 }
	var isEven: Bool { Int(self) % 2 == 0 }
	var isOdd: Bool { Int(self) % 2 == 1 }
	var int: Int? { isWhole ? Int(self) : nil }
}

public extension BinaryInteger {
	var isEven: Bool { self % 2 == 0 }
	var isOdd: Bool { self % 2 == 1 }
}

struct C2: Equatable, Hashable, AdditiveArithmetic {
	var x: Int
	var y: Int
	
	init(_ x: Int, _ y: Int) {
		self.x = x
		self.y = y
	}
	
	init(dir: Character) {
		switch dir {
		case "U": self.init(0, 1)
		case "D": self.init(0, -1)
		case "L": self.init(-1, 0)
		case "R": self.init(1, 0)
		case "N": self.init(0, 1)
		case "S": self.init(0, -1)
		case "W": self.init(-1, 0)
		case "E": self.init(1, 0)
		default: self.init(0, 0)
		}
	}
	
	static let zeroAdjacents = [(-1,0),(0,-1),(0,1),(1,0)]
	static let zeroNeighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	var adjacents: [C2] { C2.zeroAdjacents.map({ C2(x + $0.0, y + $0.1) }) }
	var neighbors: [C2] { C2.zeroNeighbors.map({ C2(x + $0.0, y + $0.1) }) }
	var adjacentsWithSelf: [C2] { C2.zeroAdjacents.map({ C2(x + $0.0, y + $0.1) }) + [self] }
	var neighborsWithSelf: [C2] { C2.zeroNeighbors.map({ C2(x + $0.0, y + $0.1) }) + [self] }
	
	static var zero: C2 = C2(0, 0)
	
	mutating func rotateLeft() {
		let tempX = x
		x = -y
		y = tempX
	}
	
	mutating func rotateRight() {
		let tempX = x
		x = y
		y = -tempX
	}
	
	mutating func rotate(left: Bool) {
		left ? rotateLeft() : rotateRight()
	}
	
	func manhattanDistance() -> Int {
		abs(x) + abs(y)
	}
	
	func vectorLength() -> Double {
		sqrt(Double(x*x + y*y))
	}
	
	static func + (lhs: C2, rhs: C2) -> C2 {
		C2(lhs.x + rhs.x, lhs.y + rhs.y)
	}
	
	static func - (lhs: C2, rhs: C2) -> C2 {
		C2(lhs.x - rhs.x, lhs.y - rhs.y)
	}
}

struct C3: Equatable, Hashable, AdditiveArithmetic {
	var x: Int
	var y: Int
	var z: Int
	
	init(_ x: Int, _ y: Int, _ z: Int) {
		self.x = x
		self.y = y
		self.z = z
	}
	
	static let zeroAdjacents = [(-1,0,0),(0,-1,0),(0,0,-1),(0,0,1),(0,1,0),(1,0,0)]
	static let zeroNeighbors = [(-1,-1,-1),(-1,-1,0),(-1,-1,1),(-1,0,-1),(-1,0,0),(-1,0,1),(-1,1,-1),(-1,1,0),(-1,1,1),
								(0,-1,-1),(0,-1,0),(0,-1,1),(0,0,-1),(0,0,1),(0,1,-1),(0,1,0),(0,1,1),
								(1,-1,-1),(1,-1,0),(1,-1,1),(1,0,-1),(1,0,0),(1,0,1),(1,1,-1),(1,1,0),(1,1,1)]
	var adjacents: [C3] { C3.zeroAdjacents.map({ C3(x + $0.0, y + $0.1, z + $0.2) }) }
	var neighbors: [C3] { C3.zeroNeighbors.map({ C3(x + $0.0, y + $0.1, z + $0.2) }) }
	var adjacentsWithSelf: [C3] { C3.zeroAdjacents.map({ C3(x + $0.0, y + $0.1, z + $0.2) }) + [self] }
	var neighborsWithSelf: [C3] { C3.zeroNeighbors.map({ C3(x + $0.0, y + $0.1, z + $0.2) }) + [self] }
	
	static var zero: C3 = C3(0, 0, 0)
	
	func manhattanDistance() -> Int {
		abs(x) + abs(y) + abs(z)
	}
	
	func vectorLength() -> Double {
		sqrt(Double(x*x + y*y + z*z))
	}
	
	static func + (lhs: C3, rhs: C3) -> C3 {
		C3(lhs.x + rhs.x, lhs.y + rhs.y, lhs.z + rhs.z)
	}
	
	static func - (lhs: C3, rhs: C3) -> C3 {
		C3(lhs.x - rhs.x, lhs.y - rhs.y, lhs.z - rhs.z)
	}
}

func MD5(of string: String) -> String {
	String(Insecure.MD5.hash(data: (string).data(using: .utf8)!).description.dropFirst(12))
}

// adapted from https://www.raywenderlich.com/947-swift-algorithm-club-swift-linked-list-data-structure
class LinkedNode<Element> {
	var value: Element
	weak var prev: LinkedNode?
	var next: LinkedNode?
	
	init (_ value: Element) {
		self.value = value
	}
}

class LinkedList<Element> {
	private var head: LinkedNode<Element>?
	private var tail: LinkedNode<Element>?

	public var isEmpty: Bool {
	return head == nil
	}

	public var first: Element? {
		return head?.value
	}

	public var last: Element? {
		return tail?.value
	}
	
	public func append(_ newElement: Element) {
		let newNode = LinkedNode(newElement)
		if let tailNode = tail {
			newNode.prev = tailNode
			tailNode.next = newNode
		} else {
			head = newNode
		}
		tail = newNode
	}
}

class LinkedCycle<Element>: CustomStringConvertible {
	private var currentNode: LinkedNode<Element>?
	
	var current: Element? { currentNode?.value }
	
	func insertNext(_ newElement: Element) {
		let newNode = LinkedNode(newElement)
		if let currentNode = currentNode {
			let next = currentNode.next
			currentNode.next = newNode
			newNode.prev = currentNode
			newNode.next = next
			next?.prev = newNode
		} else {
			newNode.prev = newNode
			newNode.next = newNode
			currentNode = newNode
		}
	}
	
	func insertPrev(_ newElement: Element) {
		let newNode = LinkedNode(newElement)
		if let currentNode = currentNode {
			let prev = currentNode.prev
			currentNode.prev = newNode
			newNode.prev = prev
			newNode.next = currentNode
			prev?.next = newNode
		} else {
			newNode.prev = newNode
			newNode.next = newNode
			currentNode = newNode
		}
	}
	
	func shiftCurrent(by n: Int) {
		if currentNode == nil { return }
		if n > 0 {
			currentNode = currentNode!.next
			shiftCurrent(by: n - 1)
		} else if n < 0 {
			currentNode = currentNode!.prev
//			print(self)
			shiftCurrent(by: n + 1)
		}
	}
	
	@discardableResult func removeAndGoToNext() -> Element? {
		let value = currentNode?.value
		if currentNode?.next === currentNode {
			currentNode = nil
			return nil
		} else {
			let prev = currentNode?.prev
			currentNode = currentNode?.next
			currentNode?.prev = prev
			prev?.next = currentNode
		}
		return value
	}
	
	public var description: String {
		var text = "["
		var node = currentNode

		repeat {
			text += "\(node!.value)"
			node = node!.next
			if node !== currentNode { text += ", " }
		} while node !== currentNode
		return text + "]"
	}
}

func bfs<T>(startingWith start: Set<T>, searchFor solution: ((T, Int, Set<T>) -> Bool) = { _,_,_ in false }, expandUsing search: (T) -> [T], continueWhile shouldContinue: (Int, Set<T>) -> Bool) {
	var steps = 0
	var found: Set<T> = []
	var current: Set<T> = start
	
	w: while shouldContinue(steps, found) && !current.isEmpty {
		steps += 1
		var next: Set<T> = []
		
		for a in current {
			for b in search(a) {
				if solution(b, steps, found) { break w }
				
				if found.insert(b).inserted {
					next.insert(b)
				}
			}
		}
		
		current = next
	}
}

// from https://stackoverflow.com/questions/28349864/algorithm-for-lcm-of-doubles-in-swift
// GCD of two numbers:
func gcd(_ a: Int, _ b: Int) -> Int {
	var (a, b) = (a, b)
	while b != 0 {
		(a, b) = (b, a % b)
	}
	return abs(a)
}

// GCD of a vector of numbers:
func gcd(_ vector: [Int]) -> Int {
	return vector.reduce(0, gcd)
}

// LCM of two numbers:
func lcm(_ a: Int, _ b: Int) -> Int {
	return (a / gcd(a, b)) * b
}

// LCM of a vector of numbers:
func lcm(_ vector: [Int]) -> Int {
	return vector.reduce(1, lcm)
}

extension Int {
	var isPrime: Bool {
		// from https://stackoverflow.com/questions/31105664/check-if-a-number-is-prime
		guard self >= 2     else { return false }
		guard self != 2     else { return true  }
		guard self % 2 != 0 else { return false }
		return !stride(from: 3, through: Int(sqrt(Double(self))), by: 2).contains { self % $0 == 0 }
	}
}

enum Operation {
	case set, inc, dec, add, sub, mod, mult, div
	case jump, jnz, jez, jgz, jlz
}

func intOrReg(val: String, reg: [String: Int]) -> Int {
	if let n = Int(val) { return n }
	return reg[val] ?? 0
}

func compute(with language: [String: Operation], program: [[String]] = inputWords(), reg: inout [String: Int], line i: inout Int) {
	
	let line = program[i]
	let v1 = intOrReg(val: line[1], reg: reg)
	let v2 = line.count < 3 ? 0 : intOrReg(val: line[2], reg: reg)
	
	switch language[line[0]] {
	case .set:
		reg[line[1]] = v2
	case .inc:
		reg[line[1], default: 0] += 1
	case .dec:
		reg[line[1], default: 0] -= 1
	case .add:
		reg[line[1], default: 0] += v2
	case .sub:
		reg[line[1], default: 0] -= v2
	case .mod:
		reg[line[1], default: 0] %= v2
	case .mult:
		reg[line[1], default: 0] *= v2
	case .div:
		reg[line[1], default: 0] /= v2
		
	case .jump:
		i += v1 - 1
	case .jnz:
		if v1 != 0 { i += v2 - 1 }
	case .jez:
		if v1 == 0 { i += v2 - 1 }
	case .jgz:
		if v1 > 0 { i += v2 - 1 }
	case .jlz:
		if v1 < 0 { i += v2 - 1 }
		
	case .none:
		break
	}
	
	i += 1
	
}

class IntcodeComputer: CustomStringConvertible {
	let originalCode: [Int: Int]
	var code: [Int: Int] = [:]
	var current: Int
	var input: () -> Int
	var output: (Int) -> Void
	
	init(program: [Int], input: @escaping (() -> Int) = { 0 }, output: @escaping ((Int) -> Void) = { _ in }) {
		for (i, v) in program.enumerated() {
			code[i] = v
		}
		originalCode = code
		current = 0
		self.input = input
		self.output = output
	}
	
	func reset() {
		code = originalCode
		current = 0
	}
	
	func int(_ pos: Int) -> Int {
		code[pos, default: 0]
	}
	
	func getValue(_ i: Int, imm: Int) -> Int {
		imm % 10 == 1 ? i : int(i)
	}
	
	func getParameters() -> (Int, Int, Int, Int) {
		var opcode = int(current)
		var parameters = (opcode % 100, 0, 0, 0)
		opcode /= 100
		
		parameters.1 = int(getValue(current + 1, imm: opcode))
		opcode /= 10
		parameters.2 = int(getValue(current + 2, imm: opcode))
		opcode /= 10
		parameters.3 = getValue(current + 3, imm: opcode)
		
		return parameters
	}
	
	func step() {
		let parameters = getParameters()
		switch parameters.0 {
		case 1: code[parameters.3] = parameters.1 + parameters.2
		case 2: code[parameters.3] = parameters.1 * parameters.2
		case 3: code[int(current + 1)] = input() // assuming no 103s
		case 4: output(parameters.1)
		case 5: if parameters.1 != 0 { current = parameters.2 - 3 }
		case 6: if parameters.1 == 0 { current = parameters.2 - 3 }
		case 7: code[parameters.3] = parameters.1 < parameters.2 ? 1 : 0
		case 8: code[parameters.3] = parameters.1 == parameters.2 ? 1 : 0
		default: break
		}
		current += [1, 4, 4, 2, 2, 3, 3, 4, 4][parameters.0]
	}
	
	func runToEnd() {
		current = 0
		
		while int(current) != 99 {
			step()
		}
	}
	
	var description: String {
		var string = ""
		for i in (code.keys.min() ?? 0)...(code.keys.max() ?? 0) {
			string += String(code[i, default: 0]) + ", "
		}
		return String(string.dropLast(2))
	}
}

// 16434972
//
