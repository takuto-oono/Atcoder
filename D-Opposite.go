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

type Coordinate struct {
	x float64
	y float64
}

func findCenter(a, b Coordinate) Coordinate {
	return Coordinate{(a.x + b.x) / 2, (a.y + b.y) / 2}
}

func abs(x float64) float64 {
	if x < 0 {
		return -x
	}
	return x
}

func calRadian(angle float64) float64 {
	return angle * math.Pi / 180.0
}

func cos(angle float64) float64 {
	return math.Cos(calRadian(angle))
}

func sin(angle float64) float64 {
	return math.Sin(calRadian(angle))
}

func main() {
	n := intInput()
	x0, y0 := intInput(), intInput()
	x1, y1 := intInput(), intInput()
	a := Coordinate{float64(x0), float64(y0)}
	b := Coordinate{float64(x1), float64(y1)}
	o := findCenter(a, b)
	ac := complex(a.x, a.y)
	oc := complex(o.x, o.y)
	parAngle := 180.0 * float64(n-2) / float64(n)
	theta := 180.0 - parAngle
	ans := oc + (ac-oc)*complex(cos(theta), sin(theta))
	fmt.Println(real(ans), imag(ans))
}
