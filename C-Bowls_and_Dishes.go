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

func createBitSearchSl(k int) [][]int {
	bitSearchSl := make([][]int, pow(2, k))
	for bits := 0; bits < (1 << uint64(k)); bits++ {
		sl := make([]int, k)
		for i := 0; i < k; i++ {
			if (bits>>uint64(i))&1 == 1 {
				sl[i] = 1
			}
		}
		bitSearchSl[bits] = sl
	}
	return bitSearchSl
}

func exchangeDishFromBit(bitSl, cdSl [][]int) [][]int {
	dishesSl := make([][]int, len(bitSl))
	for i, bits := range bitSl {
		dishes := make([]int, len(cdSl))
		for j, bit := range bits {
			if bit == 1 {
				dishes[j] = cdSl[j][1]
			}
			if bit == 0 {
				dishes[j] = cdSl[j][0]
			}
		}
		dishesSl[i] = dishes
	}
	return dishesSl
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func countIsCondition(dishes []int, abSl [][]int, n int) int {
	isDishes := map[int]bool{}
	for i := 0; i < n; i++ {
		isDishes[i+1] = false
	}
	for _, v := range dishes {
		isDishes[v] = true
	}
	cnt := 0
	for _, ab := range abSl {
		a := ab[0]
		b := ab[1]
		if isDishes[a] && isDishes[b] {
			cnt += 1
		}
	}
	return cnt

}

func fullSearch(abSl, dishesSl [][]int, n int) int {
	ans := 0
	for _, dishes := range dishesSl {
		ans = max(countIsCondition(dishes, abSl, n), ans)
	}
	return ans
}

func main() {
	n, m := intInput(), intInput()
	abSl := make([][]int, m)
	for i := 0; i < m; i++ {
		a, b := intInput(), intInput()
		abSl[i] = []int{a, b}
	}
	k := intInput()
	cdSl := make([][]int, k)
	for i := 0; i < k; i++ {
		c, d := intInput(), intInput()
		cdSl[i] = []int{c, d}
	}
	bitSl := createBitSearchSl(k)
	dishesSl := exchangeDishFromBit(bitSl, cdSl)
	fmt.Println(fullSearch(abSl, dishesSl, n))
}
