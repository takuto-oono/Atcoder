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

func sortIntIntSlice(sl [][]int, index int, rev bool) {
	if rev {
		sort.Slice(sl, func(i, j int) bool { return sl[i][index] > sl[j][index] })
	} else {
		sort.Slice(sl, func(i, j int) bool { return sl[i][index] < sl[j][index] })
	}
}

func main() {
	n, d := intInput(), intInput()
	lrSlice := [][]int{}
	for i := 0; i < n; i++ {
		lr := intSliceInput(2)
		lrSlice = append(lrSlice, lr)
	}
	sortIntIntSlice(lrSlice, 1, false)
	ans := 1
	pRange := []int{lrSlice[0][1], lrSlice[0][1] + d - 1}
	for _, lr := range lrSlice {
		l, r := lr[0], lr[1]
		if l > pRange[1] || r < pRange[0] {
			ans += 1
			pRange[0] = r
			pRange[1] = r + d - 1
		}
	}
	fmt.Println(ans)
}
