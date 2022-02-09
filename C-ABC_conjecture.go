package main

import (
	"fmt"
)

func main() {
	var n int64
	var a int64
	var b int64
	var c int64
	var ans int64
	fmt.Scan(&n)

	for a = 1; a < n + 1; a ++ {
		if a * a * a > n {
			break
		}

		for b = a; b < n + 1; b ++ {
			if b * b > n {
				break
			}

			c = n / (a * b)
			if c < b {
				break
			}

			ans += c - b + 1
		}
	}

	fmt.Println(ans)
}