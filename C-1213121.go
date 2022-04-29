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
	x, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return x
}

func largeInput() string {
	buf := make([]byte, 0, 1000000)
	for {
		l, p, e := rdr.ReadLine()
		if e != nil {
			panic(e)
		}
		buf = append(buf, l...)
		if !p {
			break
		}
	}
	return string(buf)
}

func main() {
	n := intInput()
	ans := []int{1}
	for i := 1; i < n; i ++ {
		ans = append(ans, i + 1)
		for _, v := range(ans) {
			if v == i + 1 {
				break
			}
			ans = append(ans, v)
		}
	}
	ansString := []string{}
	for _, v := range(ans) {
		ansString = append(ansString, strconv.Itoa(v))
	}
	fmt.Println(strings.Join(ansString, " "))
}
