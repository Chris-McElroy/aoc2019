//
//  day05.swift
//  aoc2019
//
//  Created by Chris McElroy on 11/25/21.
//

import Foundation

func d5() {
	let computer = IntcodeComputer(program: inputInts(","), input: { 5 }, output: { print($0) })
	
	computer.runToEnd()
}

// 16434972
// 16694270
