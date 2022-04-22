package main
import "fmt"

func main() {
	var l, ans int64
	fmt.Scan(&l)
	ans = 1
	var i int64
	for i = 0; i < 11; i ++ {
		ans *= (l - 1 - i)
		ans /= (i + 1)
	}

	fmt.Println(ans)

}