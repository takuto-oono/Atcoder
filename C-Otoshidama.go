package main
import "fmt"
import "os"

func main(){
	var n, y int
	fmt.Scan(&n, &y)
	for i := 0; i < n + 1; i ++ {
		for j := 0; j < n - i + 1; j ++ {
			if 10000 * i + 5000 * j == y - 1000 * (n - i - j) {
				fmt.Println(i, j, (n - i - j))
				os.Exit(0)
			}
		}
	}
	fmt.Println(-1, -1, -1)
}