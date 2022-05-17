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

func lowerBound(slice []int, v int) int {
	l, r := 0, len(slice)-1
	for {
		if r-l == 1 {
			break
		}
		m := (l+r)/2 + 1
		if slice[m] > v {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	return l
}

func sortIntSlice(sl *[]int, rev bool) {
	if rev {
		sort.Sort(sort.Reverse(sort.IntSlice(*sl)))
	} else {
		sort.Sort(sort.IntSlice(*sl))
	}
}

func insertAndSort(sl []int, x int, rev bool) []int {
	index := -1
	if rev {
		for i, v := range sl {
			if v < x {
				index = i
				break
			}
		}
	} else {
		for i, v := range sl {
			if v > x {
				index = i
				break
			}
		}
	}
	if index == -1 {
		sl = append(sl, x)
		return sl
	}

	return insertIntSlice(sl, x, index)
}

func insertIntSlice(sl []int, x, index int) [] int{
	l := len(sl)
	if index == l - 1 {
		sl = append(sl, x)
	} else if (index == 0) {
		sl = append(sl, sl[l - 1])
		tmp := x
		for i := 0; i < l; i ++ {
			sl[i], tmp = tmp, sl[i]
		}
	} else {
		sl = append(sl, sl[l - 1])
		tmp := x
		for i := 0; i < l; i ++ {
			if i < index {
				continue
			}
			sl[i], tmp = tmp, sl[i]
		}
	}
	return sl
}


func process1(x int, interceptSlice []int) []int {
	return insertAndSort(interceptSlice, x, false)
}

func process2(x, l int, interceptSlice []int) {
	if len(interceptSlice) == 0 {
		fmt.Println(l)
		return
	}

	if len(interceptSlice) == 1 {
		if x < interceptSlice[0] {
			fmt.Println(interceptSlice[0])
		} else {
			fmt.Println(l - interceptSlice[0])
		}
		return
	}
	ok := 0
	ng := len(interceptSlice) - 1
	for {
		if ok+1 == ng {
			break
		}
		mid := (ok + ng) / 2
		if interceptSlice[mid] < x {
			ok = mid
		} else {
			ng = mid
		}
	}
	fmt.Println(interceptSlice[ng] - interceptSlice[ok])
}

func main() {
	l, q := intInput(), intInput()
	interceptSlice := []int{0, l}
	for i := 0; i < q; i++ {
		c, x := intInput(), intInput()
		fmt.Println(interceptSlice)
		if c == 1 {
			interceptSlice = process1(x, interceptSlice)
		} else if c == 2 {
			process2(x, l, interceptSlice)
		}
	}
}
