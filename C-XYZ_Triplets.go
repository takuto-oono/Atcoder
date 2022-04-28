package main
import "fmt"

func main(){
	var n int
	fmt.Scan(&n)
	Ans := make([] int, n)
	

	for i := 1; i < 101; i ++ {
		for j := 1; j < 101; j ++ {
			for k := 1; k < 101; k ++ {
				memo := i * i + j * j + k * k + i * j + j * k + k * i
				if memo <= n {
					Ans[memo - 1] += 1
				}
			}
		}
	}

	for i := 0; i < n; i ++ {
		ans := Ans[i]
		fmt.Println(ans)
	}
}