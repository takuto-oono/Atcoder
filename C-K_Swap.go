package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
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

func sortIntSlice(sl *[]int, rev bool) {
	if rev {
		sort.Sort(sort.Reverse(sort.IntSlice(*sl)))
	} else {
		sort.Sort(sort.IntSlice(*sl))
	}
}

func sortIntIntSlice(sl [][]int) [][]int {
	for i := 0; i < len(sl); i++ {
		sortIntSlice(&sl[i], false)
	}
	return sl
}

func divideSl(k int, aSl []int) [][]int {
	dividedSl := make([][]int, k)
	for i, v := range aSl {
		m := i % k
		dividedSl[m] = append(dividedSl[m], v)
	}
	return dividedSl
}

func merge(sortedDividedSl [][]int, n, k int) []int {
	mergeSl := make([]int, n)
	for i, sl := range sortedDividedSl {
		for j, v := range sl {
			mergeSl[j*k+i] = v
		}
	}
	return mergeSl
}

func checkSorted(sl []int) bool {
	for i := 0; i < len(sl)-1; i++ {
		if sl[i+1] < sl[i] {
			return false
		}
	}
	return true
}

func main() {
	n, k := intInput(), intInput()
	aSl := intSliceInput(n)
	sortedDividedSl := sortIntIntSlice(divideSl(k, aSl))
	mergeSl := merge(sortedDividedSl, n, k)
	if checkSorted(mergeSl) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
