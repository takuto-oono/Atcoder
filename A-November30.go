package main
import "fmt"

func main() {
	var m1, d1, m2, d2, ans int
	fmt.Scan(&m1, &d1, &m2, &d2)
	if m1 == m2 {
		ans = 0
	} else {
		ans = 1
	}

	fmt.Println(ans)
}