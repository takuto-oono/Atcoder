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

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	n := intInput()
	x, y := intInput(), intInput()
	abSlice := [][]int{}
	for i := 0; i < n; i++ {
		abSlice = append(abSlice, intSliceInput(2))
	}
	dpSlice := [][][]int{}
	for i := 0; i < n+1; i++ {
		sl1 := [][]int{}
		for j := 0; j < x+1; j++ {
			sl2 := []int{}
			for k := 0; k < y+1; k++ {
				sl2 = append(sl2, 500)
			}
			sl1 = append(sl1, sl2)
		}
		dpSlice = append(dpSlice, sl1)
	}
	dpSlice[0][0][0] = 0
	for i := 1; i < n+1; i++ {
		for j := 0; j < x+1; j++ {
			for k := 0; k < y+1; k++ {
				dpSlice[i][min(x, j+abSlice[i-1][0])][min(y, k+abSlice[i-1][1])] = min(dpSlice[i][min(x, j+abSlice[i-1][0])][min(y, k+abSlice[i-1][1])], dpSlice[i-1][j][k]+1)
				dpSlice[i][j][k] = min(dpSlice[i-1][j][k], dpSlice[i][j][k])
			}
		}
	}
	ans := dpSlice[n][x][y]
	if ans == 500 {
		fmt.Println(-1)
	} else {
		fmt.Println(ans)
	}
}
