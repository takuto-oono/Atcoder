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

func createDifSl(abSl [][]int) []int {
	difSl := make([]int, len(abSl))
	for i, sl := range abSl {
		a := sl[0]
		b := sl[1]
		difSl[i] = b + a*2
	}
	return difSl
}

func sortIntSlice(sl *[]int, rev bool) {
	if rev {
		sort.Sort(sort.Reverse(sort.IntSlice(*sl)))
	} else {
		sort.Sort(sort.IntSlice(*sl))
	}
}

func calFirstDif(abSl [][]int) int {
	s := 0
	for _, sl := range abSl {
		s += sl[0]
	}
	return s
}

func findAns(abSl [][]int) int {
	difSl := createDifSl(abSl)
	sortIntSlice(&difSl, true)
	dif := calFirstDif(abSl)
	ans := 0
	for _, parDif := range difSl {
		dif -= parDif
		ans += 1
		if dif < 0 {
			break
		}
	}
	return ans
}

func main() {
	n := intInput()
	abSl := make([][]int, n)
	for i := 0; i < n; i++ {
		a, b := intInput(), intInput()
		abSl[i] = make([]int, 2)
		abSl[i][0] = a
		abSl[i][1] = b
	}
	fmt.Println(findAns(abSl))
}
