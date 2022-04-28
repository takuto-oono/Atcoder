package main
import (
	"fmt"
)

func main(){
	var n int
	var S string
	fmt.Scan(&n)
	fmt.Scan(&S)
	memo_e := [] int {0}
	memo_w := [] int {0}
	
	
	c := 0
	for i := 0; i < n; i++ {
		if S[i] == 'W' {
			c += 1
		}
		memo_w = append(memo_w, c)
	}
	c = 0
	for i := 0; i < n; i ++ {
		x := n - 1 - i
		if S[x] == 'E' {
			c += 1
		}
		memo_e = append(memo_e, c)

	}
	

	ans := 10000000000
	for i := 0; i < n + 1; i ++ {
		x := i
		y := n - i
		z := memo_w[x] + memo_e[y]
		if z < ans {
			ans = z
		}
	}
	fmt.Println(ans)
}