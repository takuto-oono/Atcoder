package main
import (
	"fmt"
)

func main(){
	var v, t, s, d int
	fmt.Scan(&v, &t, &s, &d)
	var ans string
	if v * t <= d && d <= v * s {
		ans = "No"
	} else {
		ans = "Yes"
	}

	fmt.Println(ans)
}