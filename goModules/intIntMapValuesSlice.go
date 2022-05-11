package main

import (

)

func intIntMapValuesSlice(m map[int]int) []int {
	sl := []int{}
	for _, v := range m {
		sl = append(sl, v)
	}
	return sl
}