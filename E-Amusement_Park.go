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
	sortIntSlice(&aSlice, true)
	aSlice = append(aSlice, 0)
	ans := 0
	cnt := 0
	f := true
	cntI := 0
	for i := 0; i < n; i++ {
		cntI = i
		tmp := (aSlice[i] - aSlice[i+1]) * (i + 1)
		if cnt+tmp > k {
			break
		}
		ans += (i + 1) * ((aSlice[i]) + aSlice[i+1] + 1) * (aSlice[i] - aSlice[i+1]) / 2
		cnt += tmp
		if cnt == k {
			f = false
			break
		}
		if i == n-1 {
			f = false
		}
	}

	if f {
		d := (k - cnt) / (cntI + 1)
		m := (k - cnt) % (cntI + 1)
		ans += (cntI + 1) * (aSlice[cntI] + aSlice[cntI] - d + 1) * d / 2
		ans += m * (aSlice[cntI] - d)
	}
	fmt.Println(ans)
}
