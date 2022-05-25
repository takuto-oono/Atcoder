package main

import "fmt"

func main(){
	var n, k, i int64
	fmt.Scan(&n, &k)
	for i = 0; i < k; i ++ {
		if n % 200 == 0 {
			n /= 200
		} else {
			n *= 1000
			n += 200
		}
	}
	fmt.Println(n)
}