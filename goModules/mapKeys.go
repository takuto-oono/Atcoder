package main

import (

)

func intIntMapKeysSlice(m map[int]int) []int {
	sl := []int{}
	for k, _ := range m {
		sl = append(sl, k)
	}
	return sl
}