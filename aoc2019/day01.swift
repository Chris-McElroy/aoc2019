//
//  day01.swift
//  aoc2019
//
//  Created by Chris McElroy on 11/16/21.
//

import Foundation

func d1() {
	print(inputInts().reduce(0, { $0 + $1/3 - 2 }))
	
	var sum2 = 0
	for var m in inputInts() {
		while m > 5 {
			m = m/3 - 2
			sum2 += m
		}
	}
	print(sum2)
}

// 3563458
// 5342292
