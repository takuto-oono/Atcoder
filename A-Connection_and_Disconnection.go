package main
import (
	"fmt"
)

func main(){
	var S string
	var k int
	fmt.Scan(&S)
	fmt.Scan(&k)
	S_2 := S + S
	
	memo := 0
	memo_2 := 0
	for i := 0; i < len(S_2) - 1; i++ {
		if memo == 0 {
			if S_2[i] == S_2[i + 1] {
				memo_2 += 1 
				memo = 1
			}
		} else {
			memo = 0
		}
	}
	S_3 := S_2 + S
	memo = 0
	memo_3 := 0
	for i := 0; i < len(S_3) - 1; i++ {
		if memo == 0 {
			if S_3[i] == S_3[i + 1] {
				memo_3 += 1
				memo = 1
			}
		} else {
			memo = 0
		}
	}
	
	memo = 0
	memo_1 := 0
	for i := 0; i < len(S) - 1; i++ {
		if memo == 0 {
			if S[i] == S[i + 1] {
				memo_1 += 1
				memo = 1
			}
		} else {
			memo = 0
		}
	}
	var ans int
	if k == 1 {
		ans = memo_1
	} else if k == 2 {
		ans = memo_2
	} else if k == 3 {
		ans = memo_3
	} else {
		ans = memo_1 + (memo_3 - memo_2) * (k - 1)
	}
	fmt.Println(ans)
}