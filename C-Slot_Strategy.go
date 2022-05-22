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

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func maxSlice(sl []int) int {
	if len(sl) == 0 {
		return 0
	}
	ans := sl[0]
	for _, x := range sl {
		if x > ans {
			ans = x
		}
	}
	return ans
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

func stringToInt(s string) int {
	x, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return x
}

func main() {
	n := intInput()
	sSlice := []string{}
	for i := 0; i < n; i++ {
		s := stringInput()
		sSlice = append(sSlice, s)
	}
	numCount := [][]int{}
	for i := 0; i < n; i++ {
		s := sSlice[i]
		sl := []int{}
		for j := 0; j < 10; j ++ {
			sl = append(sl, 0)
		}
		for j := 0; j < 10; j++ {
			sl[stringToInt(s[j:j+1])] = j
		}
		numCount = append(numCount, sl)

	}
	ans := 100000000000
	for i := 0; i < 10; i ++ {
		times := []int{}
		for j := 0; j < n; j ++ {
			times = append(times, numCount[j][i])
		}
		isUse := map[int]int{}
		for j, t := range times {
			if v, ok := isUse[t]; !ok {
				isUse[t] = 1
			} else {
				times[j] = v * 10 + t
				isUse[t] += 1
			}
		}
		ans = min(ans, maxSlice(times))
	}
	fmt.Println(ans)
}
