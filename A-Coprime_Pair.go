package main

import (
	"fmt"
)

func gcd(x, y int) int {
	if x > y {
		x, y = y, x
	}

	for x != 0 {
		x, y = y%x, x
	}
	return y
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func main() {
	var l, r int
	fmt.Scan(&l)
	fmt.Scan(&r)
	ans := 0
	for i := 0; i < 2000; i++ {
		for j := 0; j < 2000; j++ {
			x := l + i
			y := r - j
			if x >= y {
				continue
			}
			if gcd(x, y) == 1 {
				ans = max(ans, y-x)
			}
		}
	}
	fmt.Println(ans)
}
