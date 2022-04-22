package main

import "fmt"

func main() {
	var v, a, b, c int
	fmt.Scan(&v, &a, &b, &c)

	for {
		if v < a {
			fmt.Println("F")
			return
		}

		v -= a
		if v < b {
			fmt.Println("M")
			return
		}

		v -= b
		if v < c {
			fmt.Println("T")
			return
		}
		v -= c
	}
}
