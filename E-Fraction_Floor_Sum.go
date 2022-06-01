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

func sqrt(n, m int) int {
	ans := 1
	for i := 1; i < n+1; i++ {
		if pow(i+1, m) > n {
			break
		}
		ans = i
	}
	return ans
}

func main() {
	n := intInput()
	ans := 0
	m := sqrt(n, 2)
	for i := 1; i < m+1; i++ {
		ans += (n/i - n/(i+1)) * i
	}
	for i := 1; i < n/(m+1)+1; i++ {
		ans += n / i
	}
	fmt.Println(ans)
}
