package main
import (
	"fmt"
	"strconv"
)

func main(){
	var n, a, b int
	fmt.Scan(&n, &a, &b)
	ans := 0
	for i := 0; i < n + 1; i ++ {
		x := strconv.Itoa(i)
		
		memo := 0
		for j := 0; j < len(x); j ++ {
			y, _ := strconv.Atoi(x[j:j + 1])
			memo += y
			
		}
		if memo >= a && memo <= b {
			ans += i
		}
	}
	fmt.Println(ans)

}