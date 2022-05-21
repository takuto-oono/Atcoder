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

type Section struct {
	t int
	l float64
	r float64
}

func max(x, y float64) float64 {
	if x > y {
		return x
	}
	return y
}

func min(x, y float64) float64 {
	if x < y {
		return x
	}
	return y
}

func judge(sec1, sec2 Section) bool {
	transformSection(&sec1)
	transformSection(&sec2)
	if max(sec1.l, sec2.l) <= min(sec1.r, sec2.r) {
		return true
	}
	return false
}

func transformSection(sec *Section) {
	if sec.t == 2 {
		sec.r -= 0.5
	}
	if sec.t == 3 {
		sec.l += 0.5
	}
	if sec.t == 4 {
		sec.l += 0.5
		sec.r -= 0.5
	}
	sec.t = 1
}

func main() {
	n := intInput()
	sections := []Section{}
	for i := 0; i < n; i++ {
		t := intInput()
		l := intInput()
		r := intInput()
		section := Section{t: t, l: float64(l), r: float64(r)}
		sections = append(sections, section)
	}
	ans := 0
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			if judge(sections[i], sections[j]) {
				ans += 1
			}
		}
	}
	fmt.Println(ans)
}
