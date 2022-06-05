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

func createAnsSl(n int) [][]int {
	ansSl := make([][]int, n)
	for i := 0; i < n; i++ {
		sl := make([]int, i+1)
		for j := 0; j < i+1; j++ {
			if j == 0 || j == i {
				sl[j] = 1
			} else {
				sl[j] = ansSl[i-1][j-1] + ansSl[i-1][j]
			}
		}
		ansSl[i] = sl
	}
	return ansSl
}

func printAnsSl(ansSl [][]int) {
	for _, sl := range ansSl {
		strSl := []string{}
		for _, v := range sl {
			strSl = append(strSl, strconv.Itoa(v))
		}
		fmt.Println(strings.Join(strSl, " "))
	}
}

func main() {
	n := intInput()
	printAnsSl(createAnsSl(n))

}
