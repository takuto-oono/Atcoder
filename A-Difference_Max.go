package main

import (
	"fmt"
	
)

func main(){
	var a, b, c, d, ans int
	fmt.Scan(&a, &b)
	fmt.Scan(&c, &d)
	
	C := [4] int {a - c, a - d, b - c, b - d}
	ans = -100000000
	for i := 0; i < 4; i++ {
		if ans < C[i]{
			ans = C[i]
		}
	}
	fmt.Println(ans)
	
	

}