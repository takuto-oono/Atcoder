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

func createCountSl(n int, aSl []int) []int {
	cnt := 0
	cntSl := make([]int, n)
	for i := 0; i < n; i++ {
		if i == 0 {
			cnt += aSl[i] - 1
			cntSl[i] = cnt
			continue
		}
		cnt += aSl[i] - aSl[i-1] - 1
		cntSl[i] = cnt
	}
	return cntSl
}

func lowerBound(slice []int, v int) int {
	l, r := 0, len(slice)-1
	for l <= r {
		m := l + (r-l)/2
		if slice[m] < v {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}

func findAns(n, k int, aSl, cntSl []int) int {
	if cntSl[n-1] < k {
		return aSl[n-1] + k - cntSl[n-1]
	}
	if cntSl[0] >= k {
		return aSl[0] - (cntSl[0] - k) - 1
	}
	index := lowerBound(cntSl, k)
	return aSl[index] - (cntSl[index] - k) - 1

}

func main() {
	n, q := intInput(), intInput()
	aSl := intSliceInput(n)
	cntSl := createCountSl(n, aSl)
	for i := 0; i < q; i++ {
		k := intInput()
		fmt.Println(findAns(n, k, aSl, cntSl))
	}
}
