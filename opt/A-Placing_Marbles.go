package main
import (
	"fmt"
)

func main(){
	var S string
	fmt.Scan(&S)
	ans := 0
	if S[0] == '1' {
		ans += 1
	}
	if S[1] == '1' {
		ans += 1
	}
	if S[2] == '1' {
		ans += 1
	}

	fmt.Println(ans)
}