package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"reflect"
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

func sortIntIntSlice(sl [][]int, index int, rev bool) {
	if rev {
		sort.Slice(sl, func(i, j int) bool { return sl[i][index] > sl[j][index] })
	} else {
		sort.Slice(sl, func(i, j int) bool { return sl[i][index] < sl[j][index] })
	}
}

func createLocationInformation(sl []string, n int) [][]int {
	locationInformation := [][]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			s := sl[i][j : j+1]
			if s == "#" {
				locationInformation = append(locationInformation, []int{i, j})
			}
		}
	}
	sortIntIntSlice(locationInformation, 1, false)
	standardY := locationInformation[0][0]
	standardX := locationInformation[0][1]
	for i := 0; i < len(locationInformation); i ++ {
		locationInformation[i][0] -= standardY
		locationInformation[i][1] -= standardX
	}
	return locationInformation	
}

func lotate(sl [][]int) [][]int {
	newSl := [][]int{}
	for _, v := range sl {
		y := v[0]
		x := v[1]
		newSl = append(newSl, []int{y, -x})
	}
	return newSl
}

func isSameSliceAndSlice2(sl1, sl2 [][]int) bool {
	return reflect.DeepEqual(sl1, sl2)
}

func judge(sSlice, tSlice []string, n int ) bool {
	locationS := createLocationInformation(sSlice, n)
	locationT := createLocationInformation(tSlice, n)

	for i := 0; i < 4; i ++ {
		if isSameSliceAndSlice2(locationS, locationT) {
			return true
		}
		locationS = lotate(locationS)
	}
	return false
}

func main() {
	n := intInput()
	sSlice := []string{}
	tSlice := []string{}
	for i := 0; i < n; i++ {
		s := stringInput()
		sSlice = append(sSlice, s)
	}
	for i := 0; i < n; i++ {
		t := stringInput()
		tSlice = append(tSlice, t)
	}
	if judge(sSlice, tSlice, n) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
