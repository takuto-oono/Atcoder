package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)
	n := len(S)
	n1 := (n - 1) / 2
	n2 := (n + 3) / 2
	ans := "Yes"
	for i := 0; i < n1 / 2; i ++ {
		fmt.Println(S[i:i + 1], S[n1 - i - 1: n1 - i])
		if S[i: i + 1] != S[n1 - i - 1: n1 - i] {
			ans = "No"
		}
	}
	for i := n2 - 1; i < (n - n2 + 1) / 2 + 1; i ++ {
		fmt.Println(i, S[i: i + 1], S[n - i - 1: n - i])
		if S[i: i + 1] != S[n - i - 1: n - i] {
			ans = "No"
		}
	}
	fmt.Println(ans)

}