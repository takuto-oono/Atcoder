package main
import (
	"fmt"
)

func main(){
	var n, h int
	fmt.Scan(&n)
	H := []int{}
	for i := 0; i < n; i++ {
		fmt.Scan(&h)
		H = append(H, h)
	}
	ans := 1
	for i := 1; i < n; i++ {
		memo := 0
		for j := 0; j < i; j++ {
			if H[j] > H[i] {
				memo += 1
			}
		}
		if memo == 0 {
			ans += 1
		}
	}
	fmt.Println(ans)
}