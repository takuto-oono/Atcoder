package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var rdr = bufio.NewReaderSize(os.Stdin, 1000000)

func stringInput() string {
	sc.Scan()
	return sc.Text()
}

func intInput() int {
	sc.Scan()
	x, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return x
}

func intSliceInput(n int) []int {
	sl := []int{}
	for i := 0; i < n; i++ {
		x := intInput()
		sl = append(sl, x)
	}
	return sl
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func initSlSl(y, x int) [][]int {
	sl := make([][]int, y)
	if x == -1 {
		for i := 0; i < y; i++ {
			sl[i] = []int{}
		}
		return sl
	}
	for i := 0; i < y; i++ {
		sl[i] = make([]int, x)
	}
	return sl
}

func init() {
	sc.Split(bufio.ScanWords)
}

func printIntSlice(sl []int) {
	ans := make([]string, 0)
	for _, v := range sl {
		ans = append(ans, strconv.Itoa(v))
	}
	fmt.Println(strings.Join(ans, " "))
}

func operate(aSl []int, l, n, k, q int) []int {
	if aSl[l-1] == n {
		return aSl
	}

	if l == k {
		aSl[l-1] += 1
		return aSl
	}

	if aSl[l-1]+1 == aSl[l] {
		return aSl
	}

	aSl[l-1] += 1
	return aSl
}

func main() {
	n, k, q := intInput(), intInput(), intInput()
	aSl := intSliceInput(k)
	lSl := intSliceInput(q)
	for _, l := range lSl {
		aSl = operate(aSl, l, n, k, q)
	}
	printIntSlice(aSl)
}
