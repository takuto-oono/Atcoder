package main
import (
	"fmt"
	
)

func permutations(n, k int) int {
	v := 1
	if 0 < k && k <= n {
		for i := 0; i < k; i ++ {
			v *= (n - i)
		}
	} else if k > n {
		v = 0
	}
	return v
}

func factorial(n int) int {
	return permutations(n, n - 1)
}

func combinations(n, k int) int {
	return permutations(n, k) / factorial(k)
}
func homogeneous(n, k int) int {
	return combinations(n + k - 1, k)
}

func main(){
	var l int
	fmt.Scan(&l)
	ans := homogeneous(12, l)
	fmt.Println(ans)

}