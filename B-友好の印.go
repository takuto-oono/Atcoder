package main
import "fmt"
import "math"

func main(){
	var dt, ht, h, d, ans float64
	var n int
	fmt.Scan(&n, &dt, &ht)
	ans = -10000.0
	for i := 0; i < n; i ++ {
		fmt.Scan(&d, &h)
		ans = math.Max(ans, h - (ht - h) / (dt - d) * d)
	}
	if ans < 0 {
		ans = 0.0
	}
	fmt.Println(ans)
}