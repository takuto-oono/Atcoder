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

func removeSliceByIndex(sl []int, index int) []int {
	return sl[:index+copy(sl[index:], sl[index+1:])]
}

func DFS(graph [][]int, n int) []int {
	seenSlice := []int{}
	for i := 0; i < n; i++ {
		seenSlice = append(seenSlice, -1)
	}
	todoSlice := []int{0}
	seenSlice[0] = 0
	for {
		if len(todoSlice) == 0 {
			break
		}
		now := todoSlice[0]
		todoSlice = removeSliceByIndex(todoSlice, 0)
		dis := seenSlice[now] + 1
		for _, next := range graph[now] {
			if seenSlice[next] == -1 {
				seenSlice[next] = dis
				todoSlice = append(todoSlice, next)
			}
		}
	}
	return seenSlice
}

func Judge(dis1, dis2 int) string {
	if (dis1+dis2)%2 == 0 {
		return "Town"
	} else {
		return "Road"
	}
}

func main() {
	n, q := intInput(), intInput()
	graph := [][]int{}
	for i := 0; i < n; i++ {
		graph = append(graph, []int{})
	}
	for i := 0; i < n-1; i++ {
		a, b := intInput(), intInput()
		graph[a-1] = append(graph[a-1], b-1)
		graph[b-1] = append(graph[b-1], a-1)
	}
	disSlice := DFS(graph, n)
	for i := 0; i < q; i++ {
		c, d := intInput(), intInput()
		fmt.Println(Judge(disSlice[c-1], disSlice[d-1]))
	}
}
