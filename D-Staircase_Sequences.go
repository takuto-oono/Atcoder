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

func divisor(n int) []int {
	divisorSlice := []int{}
	for i := 1; i < n+1; i++ {
		if i*i > n {
			break
		}
		if n%i == 0 {
			divisorSlice = append(divisorSlice, i)
			if i*i != n {
				divisorSlice = append(divisorSlice, n/i)
			}
		}
	}
	return divisorSlice
}

func judge(n, m int) bool {
	l := 2 * n / m
	if l%2 == 1 && m%2 == 0 {
		return true
	}
	if l%2 == 0 && m%2 == 1 {
		return true
	}
	return false
}

func countIsCondition(divisorSl []int, n int) int {
	ans := 0
	for _, m := range divisorSl {
		if judge(n, m) {
			ans += 1
		}
	}
	return ans
}

func main() {
	n := intInput()
	divisorSl := divisor(2 * n)
	fmt.Println(countIsCondition(divisorSl, n))
}
