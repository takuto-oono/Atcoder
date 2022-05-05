package main

import (
	"bufio"
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

func judge(sSlice, tSlice []string, n int) bool {
	for i := 0; i < n; i ++ {
		s := sSlice[i]
		t := tSlice[i]
		sf := true
		tf := true
		for j := 0; j < n; j ++ {
			if i == j {
				continue
			}
			if s == sSlice[j] || s == tSlice[j] {
				sf = false
			}
			if t == sSlice[j] || t == tSlice[j] {
				tf = false
			}
		}
		if sf == false && tf == false {
			return false
		}
	}
	return true
}

func main() {
	n := intInput()
	sSlice := []string{}
	tSlice := []string{}
	for i := 0; i < n; i ++ {
		s, t := stringInput(), stringInput()
		sSlice = append(sSlice, s)
		tSlice = append(tSlice, t)
	}
	if judge(sSlice, tSlice, n) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}