package main
import "fmt"
import "math"

func main(){
	var a, b, x, v1, h, ans float64
	fmt.Scan(&a, &b, &x)
	v1 = a * b * a * 1 / 3
	if x <= v1 {
		h = 3 * x / (a * b)
		ans = math.Tan(b / h)
	} else {
		h = 3 / 2 * (b - x / (a * a))
	}


}