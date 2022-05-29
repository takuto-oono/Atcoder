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

func main() {
	n, m, k, md := intInput(), intInput(), intInput(), 998244353
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, m)
	}
	for i := 0; i < m; i++ {
		dp[0][i] = 1
	}
	for i := 1; i < n; i++ {
		s := 0
		begin := 0
		end := 0
		for j := 0; j < k; j++ {
			s += dp[i-1][j]
			begin = 0
			end = k - 1
		}
		for j := 0; j < m; j++ {
			dp[i][j] = s
			if end < m-1 {
				s += dp[i-1][end]
				end += 1
			}
			if end-begin+1 > 2*k {
				s -= dp[i-1][begin]
				begin += 1
			}
		}
	}
	ans := 0
	for j := 0; j < m; j++ {
		ans += dp[n-1][j]
		ans %= md
	}
	fmt.Println(ans % md)
}
