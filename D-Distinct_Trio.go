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
	n := intInput()
	aSl := intSliceInput(n)
	aCount := []int{}
	for i := 0; i < 2*100000+1; i++ {
		aCount = append(aCount, 0)
	}
	for _, a := range aSl {
		aCount[a] += 1
	}
	ans := n * (n - 1) * (n - 2) / 6
	for _, c := range aCount {
		if c == 0 || c == 1 {
			continue
		} else if c == 2 {
			ans -= n - 2
		} else if c == 3 {
			ans -= 1
			ans -= 3 * (n - 3)
		} else if c > 3 {
			ans -= c * (c - 1) * (c - 2) / 6
			ans -= c * (c - 1) / 2 * (n - c)
		}
	}
	fmt.Println(ans)
}
