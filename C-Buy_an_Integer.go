package main
import "fmt"

func main(){
	var a, b, x, ans, len, i int64
	fmt.Scan(&a, &b, &x)
	ans = 0
	for i = 1; i < 1000000001; i ++ {
		y := i
		len = 0
		for j := 0; j < 18; j ++ {
			if y / 10 > 0 {
				len += 1
			} else {
				break
			}
		}
		
		if a * i + b * len <= x {
			ans = i
		} else {
			break
		}
	}
	fmt.Println(ans)
}