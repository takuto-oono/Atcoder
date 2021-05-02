package main
import (
	"fmt"
)

func main(){
	var a, b, c, x int
	fmt.Scan(&a)
	fmt.Scan(&b)
	fmt.Scan(&c)
	fmt.Scan(&x)
	ans := 0
	for i := 0; i < a + 1; i ++ {
		for j := 0; j < b + 1; j ++ {
			y := 500 * i + 100 * j
			z := x - y
			if z / 50 >= 0 && z / 50 <= c {
				ans += 1
			}
		}
	}
	fmt.Println(ans)

}