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

func countIntSliceValue(sl []int) map[int]int {
	countMap := make(map[int]int)
	for _, v := range sl {
		_, ok := countMap[v]
		if ok {
			countMap[v] += 1
		} else {
			countMap[v] = 1
		}
	}
	return countMap
}

func main() {
	n := intInput()
	aSlice := intSliceInput(n)
	aCountMap := countIntSliceValue(aSlice)
	ans := 0
	for k, v := range aCountMap {
		for i := 1; i < k+1; i++ {
			if i*i > k {
				break
			}
			if k%i == 0 {
				c1, ok1 := aCountMap[i]
				if i*i == k {
					if ok1 {
						ans += v * c1 * c1
					}
					continue
				}
				c2, ok2 := aCountMap[k/i]
				if ok1 && ok2 {
					ans += c1 * c2 * v * 2
				}
			}
		}
	}
	fmt.Println(ans)
}
