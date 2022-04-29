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

func printIntSlice(sl []int) {
	ans := []string{}
	for _, v := range sl {
		ans = append(ans, strconv.Itoa(v))
	}
	fmt.Println(strings.Join(ans, " "))
}

func init() {
	sc.Split(bufio.ScanWords)
}

func main() {
	n := intInput()
	aSlice := intSliceInput(n)
	x := -1
	for i := 0; i < n-1; i++ {
		if aSlice[i]-aSlice[i+1] > 0 {
			x = aSlice[i]
			break
		}
	}
	ans := []int{}

	if x == -1 {
		x = aSlice[len(aSlice)-1]

	}
	for _, v := range aSlice {
		if v != x {
			ans = append(ans, v)
		}
	}
	printIntSlice(ans)
}
