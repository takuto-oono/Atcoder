package main

import (
	"fmt"
	"os"
)

func main(){
	var n string
	fmt.Scan(&n)
	var c int
	c = 0
	for i := 0; i < len(n); i++ {
		var x int
		x = len(n) - 1 - i
		if n[x:x + 1] == "0" {
			c += 1
		} else {
			break
		}
	}

	n = n[len(n) - c:len(n)] + n[:]
	
	for i := 0; i < len(n) / 2; i++ {
		if n[i] != n[len(n) - 1 - i] {
			fmt.Println("No")
			os.Exit(0)
		}
	}
	fmt.Println("Yes")
}