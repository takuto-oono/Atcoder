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

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func main() {
	n, w := intInput(), intInput()
	aSlice := intSliceInput(n)
	numMap := map[int]bool{}
	for _, v := range aSlice {
		numMap[v] = true
	}
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			v := aSlice[i] + aSlice[j]
			numMap[v] = true
		}
	}

	for i := 0; i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				v := aSlice[i] + aSlice[j] + aSlice[k]
				numMap[v] = true
			}
		}
	}

	ans := 0
	for k, v := range numMap {
		if k <= w && v {
			ans += 1
		}
	}
	fmt.Println(ans)
}
