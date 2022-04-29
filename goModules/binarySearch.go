package main

import ()

func lowerBound(slice []int, v int) int {
	l, r := 0, len(slice)-1
	for {
		if r-l == 1 {
			break
		}
		m := (l+r)/2 + 1
		if slice[m] > v {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}

func upperBound(slice []int, v int) int {
	l, r := 0, len(slice)-1
	for {
		if r-l == 1 {
			break
		}
		m := (r + l) / 2
		if slice[m] >= v {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}
