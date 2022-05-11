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

func intIntMapValuesSlice(m map[int]int) []int {
	sl := []int{}
	for i := 0; i < len(m); i++ {
		sl = append(sl, m[i+1])
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

func main() {
	n, q := intInput(), intInput()
	ballMap := map[int]int{}
	ballMap2 := map[int]int{}
	for i := 0; i < n; i++ {
		ballMap[i+1] = i + 1
		ballMap2[i+1] = i + 1
	}
	for i := 0; i < q; i++ {
		ball1 := intInput()
		index1 := ballMap2[ball1]
		index2 := -1
		if index1 == n {
			index2 = index1 - 1
		} else {
			index2 = index1 + 1
		}
		ball2 := ballMap[index2]
		ballMap[index1], ballMap[index2] = ballMap[index2], ballMap[index1]
		ballMap2[ball1], ballMap2[ball2] = ballMap2[ball2], ballMap2[ball1]
	}
	ansSlice := intIntMapValuesSlice(ballMap)
	printIntSlice(ansSlice)
}
