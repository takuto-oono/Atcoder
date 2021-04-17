package main
import (
	"fmt"
)

func main(){
	var x, ans int
	fmt.Scan(&x)
	ans = 1
	for i := x + 1; i <= 1000000; i ++ {
		if i % 100 == 0 {
			break
		} else {
			ans += 1
		}
	}

	fmt.Println(ans)

}