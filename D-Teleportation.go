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

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

type City struct {
	x int
	y int
}

type Magic struct {
	x int
	y int
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

func isSameValueInSlice(sl []Magic, m Magic) bool {
	for _, v := range sl {
		if v == m {
			return true
		}
	}
	return false
}

func main() {
	n := intInput()
	cities := []City{}
	for i := 0; i < n; i++ {
		x, y := intInput(), intInput()
		city := City{x: x, y: y}
		cities = append(cities, city)
	}
	magics := []Magic{}
	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			x1 := cities[i].x
			y1 := cities[i].y
			x2 := cities[j].x
			y2 := cities[j].y

			xdis := abs(x1 - x2)
			ydis := abs(y1 - y2)

			d := gcd(xdis, ydis)
			if (x1-x2)*(y1-y2) >= 0 {
				magic1 := Magic{x: xdis / d, y: ydis / d}
				magic2 := Magic{x: -(xdis / d), y: -(ydis / d)}
				magics = append(magics, magic1)
				magics = append(magics, magic2)
			} else {
				magic1 := Magic{x: -(xdis / d), y: ydis / d}
				magic2 := Magic{x: xdis / d, y: -(ydis / d)}
				magics = append(magics, magic1)
				magics = append(magics, magic2)
			}
		}
	}

	magicsMap := map[Magic]bool {}
	for _, magic := range magics {
		if _, ok := magicsMap[magic]; ok {
			continue
		}
		magicsMap[magic] = true
	}
	ans := len(magicsMap)
	fmt.Println(ans)
}