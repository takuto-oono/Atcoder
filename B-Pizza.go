package main

import (
	"fmt"
	"sort"

)

func main() {
	var n int
	fmt.Scan(&n)
	a_list := make([] int, n)
	for i := 0; i < n; i ++ {
		fmt.Scan(&a_list[i])
	}

	b_list := make([] int, n + 2)
	sum := 0
	for i := 0; i < n; i ++ {
		sum += a_list[i]
		sum %= 360
		b_list[i] = sum
	}

	b_list[n] = 0
	b_list[n + 1] = 360

	sort.Ints(b_list)

	ans := 0
	for i := 0; i < n + 1; i ++ {
		gap := b_list[i + 1] - b_list[i]
		if (gap > ans) {
			ans = gap
		}
	}

	fmt.Println(ans)

}