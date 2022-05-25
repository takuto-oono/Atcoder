package main

import "fmt"

func main() {
	var h1, m1, h2, m2, k int
	fmt.Scan(&h1, &m1, &h2, &m2, &k)
	up_time := 0
	if m2-m1 >= 0 {
		up_time += m2 - m1
		up_time += 60 * (h2 - h1)
	} else {
		up_time += m2 + (60 - m1)
		up_time += 60 * (h2 - h1 - 1)
	}
	ans := up_time - k
	fmt.Println(ans)
}
