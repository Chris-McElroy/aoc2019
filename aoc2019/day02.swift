//
//  day02.swift
//  aoc2019
//
//  Created by Chris McElroy on 11/17/21.
//

import Foundation

func d2() {
	let computer = IntcodeComputer()
	computer.code[1] = 12
	computer.code[2] = 2
	computer.runToEnd()
	print(computer.code[0]!)
	
	for i in 0..<10000 {
		computer.reset()
		computer.code[1] = i / 100
		computer.code[2] = i % 100
		computer.runToEnd()
		if computer.code[0] == 19690720 {
			print(i)
			break
		}
	}
}

// 3931283
// 6979
