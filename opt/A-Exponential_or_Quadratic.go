package main

import (
	"fmt"
	"math"
)

func main() {
	var n float64
	fmt.Scan(&n)

	if (math.Pow(2, n) > n * n) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}