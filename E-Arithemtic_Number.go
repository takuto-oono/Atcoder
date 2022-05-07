package main

import (
	"bufio"
	"fmt"
	"math"
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

func repeatString(n int, s string) string {
	ans := ""
	for i := 0; i < n; i++ {
		ans += s
	}
	return ans
}

func addCondidate(slicePtr *[]int, i, j int) {
	dis := i - j
	now := j
	x := 10*i + j
	for {
		now -= dis
		if now < 0 || now > 9 || x > pow(10, 18) {
			break
		}
		x *= 10
		x += now
		*slicePtr = append(*slicePtr, x)
	}
}

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func findAllCondidate() []int {
	condidateSlice := []int{}

	for i := 1; i < 10; i++ {
		condidateSlice = append(condidateSlice, i)
		for j := 0; j < 10; j++ {
			x := i*10 + j
			condidateSlice = append(condidateSlice, x)
			addCondidate(&condidateSlice, i, j)
		}
	}
	return condidateSlice
}

func intToString(x int) string {
	return strconv.Itoa(x)
}

func findAns(x int) int {
	condidateSlice := findAllCondidate()
	ans := pow(10, 18)
	for _, c := range condidateSlice {
		if c-x >= 0 {
			if ans > c {
				ans = c
			}
		}
	}

	return ans

}

func main() {
	x := intInput()
	fmt.Println(findAns(x))
}
