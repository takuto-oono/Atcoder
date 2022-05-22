package main

import (
	"bufio"
	"os"
	"fmt"
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

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
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

func (uni *UnionFind) isSame(x, y int) bool {
	return uni.root(x) == uni.root(y)
}

func (uni *UnionFind) unite(x, y int) bool {
	x = uni.root(x)
	y = uni.root(y)
	if x == y {
		return false
	}
	if uni.sizeSlice[x] < uni.sizeSlice[y] {
		x, y = y, x
	}
	uni.parSlice[y] = x
	uni.sizeSlice[x] += uni.sizeSlice[y]
	return true
}

func (uni *UnionFind) size(x int) int {
	return uni.sizeSlice[uni.root(x)]
}


func main() {
	n := intInput()
	aSlice := intSliceInput(n)
	pairSlice := [][2]int{}
	m := map[[2]int]bool{}
	for i := 0; i < n; i ++ {
		j := n - 1 - i
		if i >= j {
			break
		}
		if aSlice[i] == aSlice[j] {
			continue
		}
		sl := [2]int{min(aSlice[i], aSlice[j]), max(aSlice[i], aSlice[j])}
		if _, ok := m[sl]; !ok {
			m[sl] = true
			pairSlice = append(pairSlice, sl)
		}
	}
	var uni UnionFind
	uni.createStruct(2 * 100000 + 1)
	for _, pair := range pairSlice {
		uni.unite(pair[0], pair[1])
	}
	ans := 0
	for i := 0; i < 2 * 100000 + 1; i ++ {
		if uni.parSlice[i] == -1 {
			if uni.sizeSlice[i] != 1 {
				ans += uni.sizeSlice[i] - 1
			}
		}
	}
	fmt.Println(ans)
}