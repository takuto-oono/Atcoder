package main

import "bufio"
import "fmt"
import "os"
import "strconv"

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func main(){
	sc.Split(bufio.ScanWords)
	n := nextInt()
	ans := 0
	
	
	for i := 0; i < n; i ++ {
		a := nextInt()
		if i % 2 == 0 && a % 2 == 1 {
			ans += 1
		}
	}
	fmt.Println(ans)
}