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

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	q := intInput()
	ma := 0
	mi := 1000000000000
	counts := map[int]int{}
	for i := 0; i < q; i++ {
		num := intInput()
		if num == 1 {
			x := intInput()
			mi = min(mi, x)
			ma = max(ma, x)
			_, ok := counts[x]
			if ok {
				counts[x] += 1
			} else {
				counts[x] = 1
			}
		}
		if num == 2 {
			x, c := intInput(), intInput()
			_, ok := counts[x]
			if ok {
				counts[x] = max(0, counts[x]-c)
				if counts[x] == 0 {
					delete(counts, x)
					if x == mi {
						mi = 1000000000
						for k, v := range counts {
							if v != 0 {
								mi = min(mi, k)
							}
						}
					}
					if x == ma {
						ma = 0
						for k, v := range counts {
							if v != 0 {
								ma = max(ma, k)
							}
						}
					}
				}

			}
		}
		if num == 3 {
			fmt.Println(ma - mi)
		}
	}
}
