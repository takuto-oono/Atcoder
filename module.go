package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var rdr *bufio.Reader

func readlinestring() string {
	buf := make([]byte, 0, 16)
	for {
		l, p, e := rdr.ReadLine()
		if e != nil {
			fmt.Println(e.Error())
			panic(e)
		}
		buf = append(buf, l...)
		if !p {
			break
		}
	}
	return string(buf)
}

func intinput() []int {
	list := make([]int, 0)
	lines := strings.Split(readlinestring(), " ")
	for _, v := range lines {
		list = append(list, intfromstr(v))
	}

	return list
}

func intfromstr(s string) int {
	v, err := strconv.Atoi(s)
	if err != nil {
		panic("fail changing int")
	}
	return v
}

func main() {
	rdr = bufio.NewReaderSize(os.Stdin, 10000000)
	
}
