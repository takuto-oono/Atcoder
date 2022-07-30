package main

import (
	"bufio"
	"fmt"
	"math"
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
	x, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return x
}

func intSliceInput(n int) []int {
	sl := []int{}
	for i := 0; i < n; i++ {
		x := intInput()
		sl = append(sl, x)
	}
	return sl
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func initSlSl(y, x int) [][]int {
	sl := make([][]int, y)
	if x == -1 {
		for i := 0; i < y; i++ {
			sl[i] = []int{}
		}
		return sl
	}
	for i := 0; i < y; i++ {
		sl[i] = make([]int, x)
	}
	return sl
}

func init() {
	sc.Split(bufio.ScanWords)
}

type UnionFind struct {
	parSlice  []int
	sizeSlice []int
}

func createStruct(n int) *UnionFind {
	uni := new(UnionFind)
	for i := 0; i < n; i++ {
		uni.parSlice = append(uni.parSlice, -1)
		uni.sizeSlice = append(uni.sizeSlice, 1)
	}
	return uni
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

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func createGraphs(circles [][]int) [][]int {
	n := len(circles)
	graphs := make([][]int, n)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			circleI := circles[i]
			circleJ := circles[j]
			if pow(circleI[2]+circleJ[2], 2) < pow(circleI[0]-circleJ[0], 2)+pow(circleI[1]-circleJ[1], 2) {
				continue
			}
			if pow(circleI[2]-circleJ[2], 2) > pow(circleI[0]-circleJ[0], 2)+pow(circleI[1]-circleJ[1], 2) {
				continue
			}
			graphs[i] = append(graphs[i], j)
		}
	}
	return graphs
}

func isCircleOnThePoint(circle []int, x int, y int) bool {
	if pow(circle[2], 2) == pow(x-circle[0], 2)+pow(y-circle[1], 2) {
		return true
	}
	return false
}

func findCircleOnThePoint(point [2]int, circles [][]int) int {
	result := -1
	for i, circle := range circles {
		if isCircleOnThePoint(circle, point[0], point[1]) {
			result = i
			break
		}
	}
	return result
}

func mainJudge(circles [][]int, n, sx, sy, tx, ty int) bool {
	graphs := createGraphs(circles)
	uni := createStruct(n)
	for i, nextCircle := range graphs {
		for _, circle := range nextCircle {
			uni.unite(i, circle)
		}
	}
	startCircle := findCircleOnThePoint([2]int{sx, sy}, circles)
	endCircle := findCircleOnThePoint([2]int{tx, ty}, circles)
	return uni.isSame(startCircle, endCircle)
}

func main() {
	n := intInput()
	sx, sy, tx, ty := intInput(), intInput(), intInput(), intInput()
	circles := make([][]int, n)
	for i := 0; i < n; i++ {
		xyr := intSliceInput(3)
		circles[i] = xyr
	}

	if mainJudge(circles, n, sx, sy, tx, ty) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}

}
