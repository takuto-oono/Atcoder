package main
import "bufio"
import "fmt"
import "os"

var sc = bufio.NewScanner(os.Stdin)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

func main(){
	S := nextLine()
	fmt.Println(S)
}