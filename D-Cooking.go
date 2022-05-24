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

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func sumIntSlice(sl []int) int {
	cnt := 0
	for _, v := range sl {
		cnt += v
	}
	return cnt
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	n := intInput()
	tSlice := intSliceInput(n)
	s := sumIntSlice(tSlice)
	half := s / 2 + 1
	sumMap := map[int]bool{0: true}
	for _, v := range tSlice {
		m := []int{}
		for sum, b := range sumMap {
			if b {
				m = append(m, sum + v)
			}
		}
		for _, v := range m {
			if v > half {
				sumMap[v] = false
			} else {
				sumMap[v] = true
			}
		}
	}
	tmp := 10000000000000
	ans := 0
	for o1, _ := range sumMap {
		o2 := s - o1
		if abs(o1 - o2) <= tmp {
			ans = max(o1, o2)
			tmp = abs(o1 - o2)
		}
	}
	fmt.Println(ans)
}
