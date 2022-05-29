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

func gcd(x, y int) int {
	if x > y {
		x, y = y, x
	}

	for x != 0 {
		x, y = y%x, x
	}
	return y
}

func lcm(x, y int) int {
	return x * y / gcd(x, y)
}

func cal(n, a int) int {
	if a > n {
		return 0
	}
	if a == n {
		return a
	}
	na := n / a
	lasA := a * na
	s := (a + lasA) * na / 2
	return s
}

func main() {
	n, a, b := intInput(), intInput(), intInput()
	ans := (1 + n) * n / 2
	ans -= cal(n, a)
	ans -= cal(n, b)
	ans += cal(n, lcm(a, b))
	fmt.Println(ans)
}
