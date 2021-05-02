package main
import (
	"fmt"
	
)

func main(){
	var n int
	fmt.Scan(&n)
	A := make([] int, n)
	for i := 0; i < n ; i ++ {
		fmt.Scan(&A[i])
	}
	ans := 100000000
	for i := 0; i < n; i ++ {
		x := A[i]
		memo := 0
		for {
			if x % 2 == 0 {
				x /= 2
				memo += 1
			} else {
				break
			}
		}
		
		if memo < ans {
			ans = memo
		}
	}
	
	fmt.Println(ans)

}