package main

import (
	"os"
	"fmt"
	"bufio"
	"strconv"
)

var scanner = bufio.NewScanner(os.Stdin)
var reader = bufio.NewReaderSize(os.Stdin, 1000000)

func readstring() string {
	scanner.Scan()
	return scanner.Text()
}


func readString() string {
	buf := make([]byte, 0, 1000000)
	for {
		l, p, e := reader.readstring()
		if e != nil {
			panic(e)
		}

		buf = append(buf, l...)
		if !p {
			break
		}
	}

	return string(buf)
}

func readInt() int {
	scanner.Scan()
	i, e := strconv.Atoi(scanner.Text())
	if e != nil {
		panic(e)
	}

	return i
}


func main() {
	var s string
	var n int

	s = readString()
	n = readInt()

	fmt.Println(s)
	fmt.Println(n)
}







