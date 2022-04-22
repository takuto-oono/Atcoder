package main
import (
	"fmt"
)

func main() {
	var n, v, c int
	fmt.Scan(&n)
	V := []int{}
	C := []int{}
	ans := 0

	for i := 0; i < n; i++ {
		fmt.Scan(&v)
		V = append(V, v)
	}
	
	for i := 0; i < n; i++ {
		fmt.Scan(&c)
		C = append(C, c)
	}

	for i := 0; i < n; i ++ {
		x := V[i] - C[i]
		if x > 0 {
			ans += x
		}
	}
	fmt.Println(ans)
}