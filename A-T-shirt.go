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
	line := intinput()
	a, b, c, x := line[0], line[1], line[2], line[3]
	if x <= a {
		fmt.Println(1)
	} else if x > a && x <= b {
		var ans = float64(c) / float64(b-a)
		fmt.Println(ans)
	} else {
		fmt.Println(0)
	}
}
