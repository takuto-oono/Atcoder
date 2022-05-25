package main

import (
	"fmt"
	"math"
)

func main() {
	var a, v, b, w, t float64
	fmt.Scan(&a, &v, &b, &w, &t)
	if t*(v-w) >= math.Abs(a-b) {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
