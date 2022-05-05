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

func printIntSlice(sl []int) {
	ans := []string{}
	for _, v := range sl {
		ans = append(ans, strconv.Itoa(v))
	}
	fmt.Println(strings.Join(ans, " "))
}

func divide(n, m int, sl1, sl2 []int) []int {
	ans := []int{}
	sl1 = reverseIntSlice(sl1)
	sl2 = reverseIntSlice(sl2)
	y := sl1[0]
	for i := 0; i < m+1; i++ {
		x := sl2[i]
		d := x / y
		ans = append(ans, d)
		for j := 0; j < n+1; j++ {
			sl2[i+j] -= d * sl1[j]
		}
	}
	return ans
}

func reverseIntSlice(sl []int) []int {
	revSl := []int{}
	l := len(sl)
	for i := 0; i < l; i ++ {
		revSl = append(revSl, sl[l - i - 1])
	}
	return revSl
}

func main() {
	n, m := intInput(), intInput()
	aSlice := intSliceInput(n + 1)
	cSlice := intSliceInput(m + n + 1)
	bSlice := reverseIntSlice(divide(n, m, aSlice, cSlice))
	printIntSlice(bSlice)
}
