package main
import "fmt"
import "os"
func main(){
	var S string
	fmt.Scan(&S)
	a := "dream"
	b := "dreamer"
	c := "erase"
	d := "eraser"
	l := len(S)
	S += "00000000000000"
	i := 0
	for i != l {
		if S[i:i + 11] == a + d{
			i += 11
		} else if S[i:i + 13] == b + d{
			i += 13
		} else if S[i: i + 10] == a + c {
			i += 10
		} else if S[i: i + 12] == b + c {
			i += 12
		} else if S[i: i + 5] == a {
			i += 5	

		}else if S[i: i + 7] == b {
			i += 7
		
		
		
		
		
		} else if S[i:i + 6] == d {
			i += 6
		} else if S[i:i + 5] == c {
			i += 5
		} else {
			fmt.Println("NO")
			os.Exit(0)
		}
		
		
	}
	fmt.Println("YES")
}