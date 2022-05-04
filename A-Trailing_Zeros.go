package main

import (
	"bufio"
	"math"
	"os"
	"strconv"
	"fmt"
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

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func findNext(before, t int) int {
	x := pow(2, t)
	c := (before / x + 1) * x
	if c % (x * 2) != 0 {
		return c
	} else {
		return c + x
	}
}

func main() {
	n := intInput()
	tSlice := intSliceInput(n)
	aSlice := []int{0}
	for i := 0; i < n; i ++ {
		aSlice = append(aSlice, findNext(aSlice[i], tSlice[i]))
	}
	fmt.Println(aSlice[n])
	

}