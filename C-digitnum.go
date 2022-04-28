package main

import (
	"fmt"
)

var n int64
var m int64

func arithmetic_progression(n int64, m int64) int64 {
	return (1 + n) * n / 2 % m
}


func main() {
	fmt.Scan(&n)
	fmt.Println(n)
	var begin int64
	var end int64
	begin = 1
	end = 9
	m = 998244353

	
	var ans int64
	ans = 0

	for i := 0; i < 19; i ++ {
		if end > n {
			break
		}

		fmt.Println(i, begin, end)
		if end == -8446744073709551617 {
			break
		}

		ans += arithmetic_progression(end - begin + 1, m)
		ans %= m
		begin *= 10
		end = end * 10 + 9
		if (end > 1000000000000000000) {
			break
		}
	}

	if end < n {
		ans += arithmetic_progression(n - begin + 1, m)
	}

	
	ans %= m
	fmt.Println(ans)

}