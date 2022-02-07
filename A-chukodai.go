package main

import (
	"fmt"
)

func main() {
	var s string
	var a, b int
	fmt.Scan(&s)
	fmt.Scan(&a, &b)
	a -= 1
	b -= 1
	var ans string

	for i := 0; i < len(s); i ++ {
		if i == a {
			ans += s[b: b + 1]
			continue
		}

		if i == b {
			ans += s[a: a + 1]
			continue
		}

		ans += s[i: i + 1]
	}

	fmt.Println(ans)

}