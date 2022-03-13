package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var rdr *bufio.Reader

func readlinestring() []string {
	list := make([]byte, 0, 16)
	for {
		l, p, _ := rdr.ReadLine()
		list = append(list, l...)
		if !p {
			return strings.Split(string(list), " ")
		}
	}
}

func intinput() []int {
	list := make([]int, 0)
	for _, v := range readlinestring() {
		list = append(list, intfromstr(v))
	}

	return list
}

func intfromstr(s string) int {
	v, _ := strconv.Atoi(s)
	return v
}

func main() {
	rdr = bufio.NewReaderSize(os.Stdin, 10000000)
	var n int
	n = intinput()[0]
	var a_list []int
	var b_list []int
	a_list = intinput()
	b_list = intinput()
	ans1 := 0
	ans2 := 0
	for i := 0; i < n; i ++ {
		if a_list[i] == b_list[i] {
			ans1++
		}
	}

	for i, a := range a_list {
		for j, b := range b_list {
			if a == b && i != j {
				ans2++
			}
		}
	}

	fmt.Println(ans1)
	fmt.Println(ans2)
}
