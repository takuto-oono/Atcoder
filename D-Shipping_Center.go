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
	n, m, q := intInput(), intInput(), intInput()
	packageSl := make([][]int, n)
	for i := 0; i < n; i++ {
		w, v := intInput(), intInput()
		packageSl[i] = []int{w, v}
	}
	sortIntIntSlice(packageSl, 1, true)
	boxSl := intSliceInput(m)
	for i := 0; i < q; i++ {
		l, r := intInput(), intInput()
		ans := 0
		isUsedBox := make([]bool, m)
		for k := 0; k < m; k++ {
			isUsedBox[k] = false
		}
		for _, pkg := range packageSl {
			tmp := 1000000000000
			usedBoxNum := -1
			for k, box := range boxSl {
				if l <= k+1 && k+1 <= r {
					continue
				}
				if isUsedBox[k] {
					continue
				}
				if box < tmp && pkg[0] <= box {
					tmp = box
					usedBoxNum = k
				}
			}
			if usedBoxNum != -1 {
				isUsedBox[usedBoxNum] = true
				ans += pkg[1]
			}
		}
		fmt.Println(ans)
	}
}
