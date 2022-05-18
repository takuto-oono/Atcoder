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

type Edge struct {
	to int
	w  int
}

type UnionFind struct {
	parSlice  []int
	sizeSlice []int
}

func (uni *UnionFind) createStruct(n int) {
	for i := 0; i < n; i++ {
		uni.parSlice = append(uni.parSlice, -1)
		uni.sizeSlice = append(uni.sizeSlice, 1)
	}
}

func (uni *UnionFind) root(x int) int {
	if uni.parSlice[x] == -1 {
		return x
	} else {
		uni.parSlice[x] = uni.root(uni.parSlice[x])
		return uni.parSlice[x]
	}
}

func (uni UnionFind) isSame(x, y int) bool {
	return uni.root(x) == uni.root(y)
}

func (uni UnionFind) unite(x, y int) bool {
	x = uni.root(x)
	y = uni.root(y)
	if x == y {
		return false
	}
	if uni.sizeSlice[x] < uni.sizeSlice[y] {
		x, y = y, x
	}
	uni.parSlice[y] = x
	uni.sizeSlice[x] = uni.sizeSlice[y]
	return true
}

func (uni UnionFind) size(x int) int {
	return uni.sizeSlice[uni.root(x)]
}

func removeSliceByIndex(sl []int, index int) []int {
	return sl[:index+copy(sl[index:], sl[index+1:])]
}

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

func sortIntIntSlice(sl [][]int, index int, rev bool) {
	if rev {
		sort.Slice(sl, func(i, j int) bool { return sl[i][index] > sl[j][index] })
	} else {
		sort.Slice(sl, func(i, j int) bool { return sl[i][index] < sl[j][index] })
	}
}

func main() {
	n, m := intInput(), intInput()
	graphSlice := [][]int{}
	ans := 0
	for i := 0; i < m; i++ {
		a, b, c := intInput(), intInput(), intInput()
		a -= 1
		b -= 1
		graphSlice = append(graphSlice, []int{a, b, c})
		ans += c
	}
	sortIntIntSlice(graphSlice, 2, false)
	fmt.Println(n)
	fmt.Println(graphSlice)
	var union UnionFind
	union.createStruct(n)
	fmt.Println(union.parSlice)
	c := 0
	for _, edge := range graphSlice {
		x := edge[0]
		y := edge[1]
		w := edge[2]
		if union.isSame(x, y) {
			continue
		}
		c += w
		union.unite(x, y)
	}
	ans -= c
	fmt.Println(ans)
}
