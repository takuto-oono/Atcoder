package main
import (
	"fmt"
	"sort"
)
func min(list []int) int {
	sort.Sort(sort.IntSlice(list))
	return list[0]
}

func main() {
	var n int
	fmt.Scan(&n)
	A := make([] int, n)
	for i := 0; i < n; i ++ {
		fmt.Scan(&A[i])
	}
	ans := 0
	for i := 0; i < n; i ++ {
		x := A[i]
		for j := i; j < n; j ++ {
			if A[j] < x {
				x = A[j]
			}
			condidate := x * (j - i + 1)
			if ans < condidate {
				ans = condidate
			}
		}
	}
	fmt.Println(ans)

}