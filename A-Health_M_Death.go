package main
import (
	"fmt"
)

func main(){
	var m, h int
	fmt.Scan(&m, &h)
	var ans string
	if h % m == 0 {
		ans = "Yes"
	} else {
		ans = "No"
	}

	fmt.Println(ans)

}