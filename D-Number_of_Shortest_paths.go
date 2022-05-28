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

func removeSliceByIndex(sl [][]int, index int) [][]int {
	return sl[:index+copy(sl[index:], sl[index+1:])]
}

func BFS(graph [][]int, n int) int {
	md := 1000000000 + 7
	times := []int{}
	counts := []int{}

	for i := 0; i < n; i++ {
		times = append(times, -1)
		counts = append(counts, 0)
	}
	counts[0] = 1
	times[0] = 0
	todoSlice := []int{0}
	i := 0
	for {
		if i == len(todoSlice) {
			break
		}
		nowCity := todoSlice[i]
		for _, nextCity := range graph[nowCity] {
			if times[nextCity] == -1 {
				times[nextCity] = times[nowCity] + 1
				counts[nextCity] = counts[nowCity]
				todoSlice = append(todoSlice, nextCity)
			} else if times[nextCity] == times[nowCity]+1 {
				counts[nextCity] += counts[nowCity]
				counts[nextCity] %= md
			}
		}
		i++
	}
	return counts[n-1] % md
}

func main() {
	n, m := intInput(), intInput()
	graph := [][]int{}
	for i := 0; i < n; i++ {
		graph = append(graph, []int{})
	}
	for i := 0; i < m; i++ {
		a, b := intInput(), intInput()
		a -= 1
		b -= 1
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	fmt.Println(BFS(graph, n))

}
