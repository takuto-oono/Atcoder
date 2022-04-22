package main

import "fmt"

func main(){
	var n, k, r, s, p, ans int
	var T string
	fmt.Scan(&n, &k)
	fmt.Scan(&r, &s, &p)
	fmt.Scan(&T)

	memo := [] int {}
	for i := 0; i < n; i ++ {
		memo = append(memo, 0)
	}
	ans = 0
	for i := 0; i < n; i ++ {
		if i - k >= 0 {
			if T[i] != T[i - k] || memo[i - k] == 0 {
				if T[i] == 's' {
					ans += r
				} else if T[i] == 'p' {
					ans += s
				} else if T[i] == 'r' {
					ans += p
				}
				memo[i] = 1
			} 
			
		} else {
			if T[i] == 's' {
				ans += r
			} else if T[i] == 'p' {
				ans += s
			} else if T[i] == 'r' {
				ans += p
			}
			memo[i] = 1
		}
		

	}
	fmt.Println(ans)
	
	
}