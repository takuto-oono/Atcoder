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

func main() {
	n, k := intInput(), intInput()
	aSlice := intSliceInput(n)
	aSliceCopy := make([]int, len(aSlice))
	copy(aSliceCopy, aSlice)
	peopleMap := map[int]int{}
	for _, num := range aSlice {
		peopleMap[num] = k / n
	}
	m := k % n
	if m > 0 {
		sortIntSlice(&aSlice, false)
		for i := 0; i < m; i++ {
			peopleMap[aSlice[i]] += 1
		}
	}
	for _, num := range aSliceCopy {
		fmt.Println(peopleMap[num])
	}
}
