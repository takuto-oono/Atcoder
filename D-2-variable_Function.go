package main

import (
	"bufio"
	"fmt"
	"math"
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

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func f(a, b int) int {
	return a * a * a + b * b * b + a*a*b + b*b*a
}

func main() {
	n := intInput()
	ans := math.MaxInt64
	for a := 0; a < 1010101; a++ {
		ng, ok := -1, 1010101
		for {
			if ng+1 == ok {
				break
			}
			m := (ok + ng) / 2
			if f(a, m) >= n {
				ok = m
			} else {
				ng = m
			}
		}
		if f(a, ok) < ans {
			ans = f(a, ok)
		}
	}
	fmt.Println(ans)
}
