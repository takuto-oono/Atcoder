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

func countTraps(aSlice []int, w int) int {
	now := 0
	cnt := 0
	for _, a := range aSlice {
		if now < a {
			cnt += (a - now + w - 1) / w
		}
		now = a + w
	}
	return cnt
}

func main() {
	n, l, w := intInput(), intInput(), intInput()
	aSlice := intSliceInput(n)
	aSlice = append(aSlice, l)
	fmt.Println(countTraps(aSlice, w))
}
