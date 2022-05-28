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

func createBitSearchSlice(n int) [][]int {
	searchSlice := make([][]int, pow(2, n))
	for bit := 0; bit < (1 << uint64(n)); bit++ {
		sl := make([]int, 0)
		for i := 0; i < n; i++ {
			if (bit >> uint64(i) & 1) == 1 {
				sl = append(sl, i)
			}
		}
		searchSlice[bit] = sl
	}
	return searchSlice
}

func separateSlice(separationSlice, aSlice []int, n int) [][]int {
	for i := 0; i < len(separationSlice); i++ {
		separationSlice[i]++
	}
	separationSlice = append([]int{0}, separationSlice[0:]...)
	separationSlice = append(separationSlice, n)
	separatedSl := make([][]int, 0)
	for i := 0; i < len(separationSlice)-1; i++ {
		separatedSl = append(separatedSl, aSlice[separationSlice[i]:separationSlice[i+1]])
	}
	return separatedSl
}

func createORSl(separatedSl [][]int) []int {
	ORSl := make([]int, len(separatedSl))
	for i, sl := range separatedSl {
		ans := sl[0]
		for j := 1; j < len(sl); j++ {
			ans = ans | sl[j]
		}
		ORSl[i] = ans
	}
	return ORSl
}

func calXOR(ORSl []int) int {
	xor := ORSl[0]
	for i := 1; i < len(ORSl); i++ {
		xor = xor ^ ORSl[i]
	}
	return xor
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	n := intInput()
	aSlice := intSliceInput(n)
	bitSl := createBitSearchSlice(n - 1)
	ans := 1000000000000000000
	for _, sl := range bitSl {
		separatedSl := separateSlice(sl, aSlice, n)
		ORSl := createORSl(separatedSl)
		ans = min(ans, calXOR(ORSl))
	}
	fmt.Println(ans)
}
