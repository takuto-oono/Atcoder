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

func countMapTrue(m map[int]bool) int {
	cnt := 0
	for _, f := range m {
		if f {
			cnt += 1
		}
	}
	return cnt
}

func DFS(graph [][]int, n int) int {
	ans := 0
	for i := 0; i < n; i++ {
		now := i
		todo := []int{now}
		seen := map[int]bool{}
		for i := 0; i < n; i++ {
			seen[i] = false
		}
		for {
			if len(todo) == 0 {
				break
			}
			now = todo[0]
			seen[now] = true
			todo = removeSliceByIndex(todo, 0)
			for _, next := range graph[now] {
				if seen[next] == false {
					todo = append(todo, next)
				}
			}
		}
		ans += countMapTrue(seen)
	}
	return ans
}

func main() {
	n, m := intInput(), intInput()
	graph := [][]int{}
	for i := 0; i < n; i++ {
		graph = append(graph, []int{})
	}
	for i := 0; i < m; i++ {
		a, b := intInput(), intInput()
		graph[a-1] = append(graph[a-1], b-1)
	}
	fmt.Println(DFS(graph, n))
}
