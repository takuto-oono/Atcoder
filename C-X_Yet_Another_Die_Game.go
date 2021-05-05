package main
import "fmt"

func main(){
	var x, ans, y int64
	fmt.Scan(&x)
	y = x % 11
	if y == 0 {
		ans = x / 11 * 2
	} else if y > 0 && y <= 6 {
		ans = x / 11 * 2 + 1
	} else if y >= 7 && y <= 10 {
		ans = x / 11 * 2 + 2
	}
	fmt.Println(ans)

}