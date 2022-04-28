package main
import (
	"fmt"
)

func main(){
	var a, b, ans float64
	fmt.Scan(&a, &b)
	ans = 100 - b / a * 100
	fmt.Println(ans)
}