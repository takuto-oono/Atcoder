package main

import (

)

func reverseIntSlice(sl []int) []int {
	revSl := []int{}
	l := len(sl)
	for i := 0; i < l; i ++ {
		revSl = append(revSl, sl[l - i - 1])
	}
	return revSl
}
