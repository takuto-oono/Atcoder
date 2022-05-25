package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)
	ans := 0
	if n % 100 == 0 {
		ans = n / 100
	} else {
		ans = n / 100 + 1
	}

	fmt.Println((ans))

}
