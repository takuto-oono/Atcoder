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
	A := make([] int, n)
	for i := 0; i < n; i ++ {
		A[i] = nextInt()
	}
	fmt.Println(A)
}