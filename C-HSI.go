package main
import (
	"fmt"
	"math"
)

func main(){
	var n, m float64
	fmt.Scan(&n, &m)
	ans := ((n - m) * 100 + 1900 * m) * math.Pow(2, m)
	fmt.Println(ans)


	
}