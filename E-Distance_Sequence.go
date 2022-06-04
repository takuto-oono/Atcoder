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

func largeInput() string {
	buf := make([]byte, 0, 1000000)
	for {
		l, p, err := rdr.ReadLine()
		if err != nil {
			panic(err)
		}
		buf = append(buf, l...)
		if !p {
			break
		}
	}
	return string(buf)
}

func intSliceInput(n int) []int {
	sl := []int{}
	for i := 0; i < n; i++ {
		x := intInput()
		sl = append(sl, x)
	}
	return sl
}

func init() {
	sc.Split(bufio.ScanWords)
}

func sumIntSlice(sl []int) int {
	s := 0
	for _, v := range sl {
		s += v
	}
	return s
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func dp(n, m, k, md int) int {
	dpSl := make([][]int, n)
	for i := 0; i < n; i++ {
		dpSl[i] = make([]int, m)
	}
	for i := 0; i < m; i++ {
		if i+k < m || i-k >= 0 {
			dpSl[0][i] = 1
		}
	}
	for i := 1; i < n; i++ {
		cumulative := 0
		for j := 0; j < m; j++ {
			if j >= k {
				cumulative += dpSl[i-1][j]
			}
		}
		cumulative %= md
		for j := 0; j < m; j++ {
			dpSl[i][j] = cumulative
			if k == 0 {
				continue
			}
			if j+k < m {
				cumulative -= dpSl[i-1][j+k]
			}
			if j >= k-1 {
				cumulative += dpSl[i-1][j-k+1]
			}
			cumulative %= md
		}
	}
	return sumIntSlice(dpSl[n-1]) % md
}

func main() {
	n, m, k, md := intInput(), intInput(), intInput(), 998244353
	fmt.Println(dp(n, m, k, md))
}
