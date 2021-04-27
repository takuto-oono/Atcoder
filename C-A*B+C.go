package main
import (
	"fmt"
)

func main(){
	var n int
	fmt.Scan(&n)
	ans := 0
	for i := 0; i < n; i ++ {
		x := i + 1
		y := n / x
		ans += y
		if x * y == n {
			ans -= 1
		}
	}

	fmt.Println(ans)
}