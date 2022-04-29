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

func createMap(list []int) map[int][]int {
	numMap := map[int][]int{}
	for i, v := range list {
		_, flag := numMap[v]
		if flag {
			numMap[v] = append(numMap[v], i+1)
		} else {
			numMap[v] = []int{i + 1}
		}
	}
	return numMap
}

func lowerBound(slice []int, v int) int {
	l, r := 0, len(slice)-1
	for {
		if l <= r {
			m := l + (r-l)/2
			if slice[m] < v {
				l = m + 1
			} else {
				r = m - 1
			}
		} else {
			return l
		}
	}
}

func upperBound(slice []int, v int) int {
	l, r := 0, len(slice)-1
	for {
		if l <= r {
			m := l + (r-l)/2
			if slice[m] <= v {
				l = m + 1
			} else {
				r = m - 1
			}

		} else {
			return l
		}
	}
}

func createAns(l, r, x int, aMap map[int][]int) int {
	_, f := aMap[x]
	if !f {
		return 0
	}
	return upperBound(aMap[x], r) - lowerBound(aMap[x], l)
}

func main() {
	sc.Split(bufio.ScanWords)

	n := intInput()
	aList := []int{}
	var a int
	for i := 0; i < n; i++ {
		a = intInput()
		aList = append(aList, a)
	}
	aMap := createMap(aList)

	q := intInput()
	for i := 0; i < q; i++ {
		l, r, x := intInput(), intInput(), intInput()
		fmt.Println(createAns(l, r, x, aMap))
	}
}
