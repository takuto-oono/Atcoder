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

func intSliceInput(n int) []int {
	sl := []int{}
	for i := 0; i < n; i++ {
		x := intInput()
		sl = append(sl, x)
	}
	return sl
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

func initSlSl(y, x int) [][]int {
	sl := make([][]int, y)
	if x == -1 {
		for i := 0; i < y; i++ {
			sl[i] = []int{}
		}
		return sl
	}
	for i := 0; i < y; i++ {
		sl[i] = make([]int, x)
	}
	return sl
}

func init() {
	sc.Split(bufio.ScanWords)
}

type Rotation struct {
	First int
	Str   string
	Len   int
}

func newRotation(str string, n int) *Rotation {
	return &Rotation{
		First: 0,
		Str:   str,
		Len:   n,
	}
}

func (rotation *Rotation) rotate(x int) {
	x %= rotation.Len
	if rotation.First-x >= 0 {
		rotation.First -= x
	} else {
		x -= rotation.First
		rotation.First = rotation.Len - x
	}
}

func printChar(s string, i int) {
	fmt.Println(s[i : i+1])
}

func (rotation *Rotation) print(x int) {
	x -= 1
	if rotation.First+x < rotation.Len {
		printChar(rotation.Str, rotation.First+x)
	} else {
		printChar(rotation.Str, (rotation.First+x)%rotation.Len)
	}
}

func main() {
	n, q := intInput(), intInput()
	s := stringInput()
	rotation := newRotation(s, n)
	for i := 0; i < q; i++ {
		t, x := intInput(), intInput()
		if t == 1 {
			rotation.rotate(x)
		}
		if t == 2 {
			rotation.print(x)
		}
	}
}
