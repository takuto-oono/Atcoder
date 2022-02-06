package main

import (
	"fmt"
)

func main() {
	fmt.Println(999999999999999999 < 1000000000000000000)
	c := 0
	x := 1000000000000000000
	for i := 0; i < 100; i ++ {
		if x == 1 {
			break
		}

		c += 1
		x /= 10
	}

	fmt.Println(c)
}