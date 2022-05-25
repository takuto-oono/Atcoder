package main

import (
	"bufio"

)
import "fmt"
import "os"
import "strconv"
import "sort"

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
	k := nextInt()
	A := make([] int, n)
	for i := 0; i < n; i ++ {
		A[i] = nextInt()
	}
	ans := 0
	B := make([] int, n + 1)

	for i := 0; i < n; i ++ {
		B[A[i]] += 1
	}
	for i := 0; i < n + 1; i ++ {
		if k > B[i] {
			ans += (k - B[i]) * i
			k = B[i]
		}
		if i == n {
			sort.Sort(sort.IntSlice(A))
			ans += (A[n - 1] + 1) * k
		}

	}
	fmt.Println(ans)
}
