package main
import "fmt"

func main(){
	var S string
	fmt.Scan(&S)
	ans := 0
	for i := 0; i < 12 - 3; i ++ {
		T := S[i:i + 4]
		
		if T == "ZONe" {
			ans += 1
		}
	}
	fmt.Println(ans)
}