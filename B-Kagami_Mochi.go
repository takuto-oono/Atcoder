package main
import "fmt"
import "sort"

func main(){
	var n int
	fmt.Scan(&n)
	D := make([] int, n)
	for i := 0; i < n; i ++ {
		fmt.Scan(&D[i])
	}

	sort.Ints(D)
	A := [] int {D[0]}
	for i := 1; i < n; i ++ {
		if D[i - 1] != D[i] {
			A = append(A, D[i])
		}
	}
	ans := len(A)
	fmt.Println(ans)

}