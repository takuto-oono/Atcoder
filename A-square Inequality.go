package main
import (
	"fmt"
)

func main(){
	var a, b, c int
	fmt.Scan(&a, &b, &c)
	var ans string
	if a * a + b * b < c * c {
		ans = "Yes"
	} else {
		ans = "No"
	}

	fmt.Println(ans)

}