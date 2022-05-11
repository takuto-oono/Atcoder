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
	n, a, b := intInput(), intInput(), intInput()
	ansSlice := [][]string{}

	for y := 0; y < a * n; y ++ {
		rowSlice := []string{}
		for x := 0; x < b * n; x ++ {
			color := 1
			yMod := y % (2 * a)
			xMod := x % (2 * b)
			if yMod >= a {
				color *= -1
			}
			if xMod >= b {
				color *= -1
			}
			if color == 1 {
				rowSlice = append(rowSlice, ".")
			} else {
				rowSlice = append(rowSlice, "#")
			}
		}
		ansSlice = append(ansSlice, rowSlice)
	}
	for _, ans := range ansSlice {
		fmt.Println(strings.Join(ans, ""))
	}
}
