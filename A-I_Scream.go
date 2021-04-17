package main
import (
	"fmt"
)
func main() {
	var a, b int
	fmt.Scan(&a, &b)
	var c, ans int
	c = a + b

	if c >= 15 && b >= 8 {
		ans = 1
	} else if c >= 10 && b >= 3 {
		ans = 2
	} else if c >= 3 {
		ans = 3
	} else {
		ans = 4
	}

	fmt.Println(ans)
}