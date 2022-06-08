package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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

func dp(n int, sSl []string) int {
	dpSl := initSlSl(n+1, 2)
	dpSl[0][0] = 1
	dpSl[0][1] = 1
	for i := 0; i < n; i++ {
		if sSl[i] == "AND" {
			dpSl[i+1][0] = dpSl[i][0]
			dpSl[i+1][1] = dpSl[i][0] + 2*dpSl[i][1]
		} else {
			dpSl[i+1][0] = 2*dpSl[i][0] + dpSl[i][1]
			dpSl[i+1][1] = dpSl[i][1]
		}
	}
	return dpSl[n][0]
}

func main() {
	n := intInput()
	sSl := make([]string, n)
	for i := 0; i < n; i++ {
		s := stringInput()
		sSl[i] = s
	}
	fmt.Println(dp(n, sSl))
}
