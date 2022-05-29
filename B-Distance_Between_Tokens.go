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

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	h, w := intInput(), intInput()
	sSl := make([]string, h)
	for i := 0; i < h; i++ {
		str := stringInput()
		sSl[i] = str
	}
	positions := [][]int{}
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			if sSl[i][j:j+1] == "o" {
				positions = append(positions, []int{i, j})
			}
		}
	}
	ans := abs(positions[0][0]-positions[1][0]) + abs(positions[0][1]-positions[1][1])
	fmt.Println(ans)
}
