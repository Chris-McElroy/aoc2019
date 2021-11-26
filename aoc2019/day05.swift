//
//  day05.swift
//  aoc2019
//
//  Created by Chris McElroy on 11/25/21.
//

import Foundation

func d5() {
	let computer = IntcodeComputer(program: inputInts(","), input: { 1 }, output: { if $0 != 0 { print($0) } })
	computer.runToEnd()
	
	computer.reset()
	computer.input = { 5 }
	computer.runToEnd()
}

// 16434972
// 16694270
