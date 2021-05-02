package main
import (
	"fmt"
	"sort"
)
func main(){
	var n int
	fmt.Scan(&n)
	A := make([] int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}
	ans := 0
	sort.Ints(A)
	B := make([] int, n)
	for i := 0; i < n; i ++ {
		B[i] = A[n - i - 1]
	}
	for i := 0; i < n; i ++ {
		if i % 2 == 0 {
			ans += B[i]
		} else {
			ans -= B[i]
		}
	}
	fmt.Println(ans)
}