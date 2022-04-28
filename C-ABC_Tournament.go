package main

import (
	"fmt"
	"math"
	
)

func main(){
	var l int
	fmt.Scan(&l)
	n := 1
	for i := 0; i < l; i ++ {
		n *= 2
	}
	A := make([] int, n)
	for i := 0; i < n; i ++ {
		fmt.Scan(&A[i])
	}
	condidate_left := 0.0
	condidate_right := 0.0
	for i := 0; i < n / 2; i ++ {
		condidate_left = math.Max(condidate_left, float64(A[i]))
	}

	for i := n / 2; i < n; i++ {
		condidate_right = math.Max(condidate_right, float64(A[i]))
	}

	ans_obj := int(math.Min(condidate_left, condidate_right))
	ans := 0
	for i := 0; i < n; i ++ {
		if ans_obj == A[i] {
			ans = i + 1
			break
		}
	}
	fmt.Println(ans)


}