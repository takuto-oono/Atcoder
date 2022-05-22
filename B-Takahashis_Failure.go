package main

import (
	"bufio"
	"os"
	"fmt"
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

func judge(bSlice, aMaxIndex []int) bool {
	for _, a := range aMaxIndex {
		for _, b := range bSlice {
			if a + 1 == b {
				return true
			}
		}
	}
	return false
}

func main() {
	n, k := intInput(), intInput()
	aSlice := intSliceInput(n)
	bSlice := intSliceInput(k)
	aMax := maxSlice(aSlice)
	aMaxIndex := []int{}
	for i, v := range aSlice {
		if v == aMax {
			aMaxIndex = append(aMaxIndex, i)
		}
	}
	if judge(bSlice, aMaxIndex) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
	
	
}