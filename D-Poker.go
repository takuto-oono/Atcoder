package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
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

func intToString(x int) string {
	return strconv.Itoa(x)
}

func createNumMap(st string, n int) map[string]int {
	numMap := map[string]int{}
	for i := 0; i < 9; i++ {
		numMap[intToString(i+1)] = n
	}
	for i := 0; i < len(st); i++ {
		s := st[i : i+1]
		if s != "#" {
			numMap[s] -= 1
		}
	}
	return numMap
}

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func cal(s string, x int) int {
	ans := 0
	for i := 1; i < 10; i++ {
		if x == i {
			ans += i * pow(10, 1+strings.Count(s, intToString(i)))
		} else {
			ans += i * pow(10, strings.Count(s, intToString(i)))
		}
	}
	return ans
}

func fullSearch(numMap map[string]int, s, t string) [][]string {
	winPatterns := [][]string{}
	for i := 1; i < 10; i++ {
		for j := 1; j < 10; j++ {
			if i == j {
				if numMap[intToString(i)] <= 1 {
					continue
				}
			}
			if numMap[intToString(j)] == 0 {
				continue
			}
			if numMap[intToString(i)] == 0 {
				continue
			}
			if cal(s, i) > cal(t, j) {
				winPatterns = append(winPatterns, []string{intToString(i), intToString(j)})
			}
		}
	}
	return winPatterns
}

func calProbability(winPatterns [][]string, k int, numMap map[string]int) float64 {
	ans := 0.0
	for _, pattern := range winPatterns {
		x := pattern[0]
		y := pattern[1]
		if x == y {
			ans += float64(numMap[x] * (numMap[x] - 1))
		} else {
			ans += float64(numMap[x] * numMap[y])
		}
	}
	ans /= float64((9*k - 8) * (9*k - 9))
	return ans
}

func main() {
	k := intInput()
	s := stringInput()
	t := stringInput()
	numMap := createNumMap(s+t, k)
	winPatterns := fullSearch(numMap, s, t)
	fmt.Println(calProbability(winPatterns, k, numMap))
}
