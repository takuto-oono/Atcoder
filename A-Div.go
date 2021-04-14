package main

import (
	"fmt"
)

func main(){
	var n int
	fmt.Scan(&n)
	var ans int
	if (n == 1){
		ans = 0
	} else {
		ans = n - 1
	}

	fmt.Println(ans)
}