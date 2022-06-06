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

func createDifSl(sl []int) []int {
	if len(sl) <= 1 {
		return []int{-1}
	}
	difSl := make([]int, len(sl)-1)
	for i := 0; i < len(sl)-1; i++ {
		difSl[i] = sl[i+1] - sl[i]
	}
	return difSl
}

func createWhiteStampSeriesSl(difSl, aSl []int, n, m int) []int {
	if aSl[0] != 1 {
		difSl = append(difSl, aSl[0])
	}

	if aSl[m-1] != n {
		difSl = append(difSl, n+1-aSl[m-1])
	}
	whiteStampSeriesSl := []int{}
	for _, dif := range difSl {
		if dif-1 != 0 {
			whiteStampSeriesSl = append(whiteStampSeriesSl, dif-1)
		}
	}
	return whiteStampSeriesSl
}

func calAns(k int, whiteStampSeriesSl []int) int {
	ans := 0
	for _, v := range whiteStampSeriesSl {
		if v%k == 0 {
			ans += v / k
		} else {
			ans += v/k + 1
		}
	}
	return ans
}

func sortIntSlice(sl *[]int, rev bool) {
	if rev {
		sort.Sort(sort.Reverse(sort.IntSlice(*sl)))
	} else {
		sort.Sort(sort.IntSlice(*sl))
	}
}

func minSl(sl []int) int {
	if len(sl) == 0 {
		return -1
	}
	mi := sl[0]
	for _, v := range sl {
		if v < mi {
			mi = v
		}
	}
	return mi
}

func main() {
	n, m := intInput(), intInput()
	aSl := intSliceInput(m)
	if m == 0 {
		fmt.Println(1)
	} else if n == m {
		fmt.Println(0)
	} else {
		sortIntSlice(&aSl, false)
		whiteStampSeriesSl := createWhiteStampSeriesSl(createDifSl(aSl), aSl, n, m)
		k := minSl(whiteStampSeriesSl)
		fmt.Println(calAns(k, whiteStampSeriesSl))
	}
}
