package main

import (
	"fmt"
	"bufio"
	"strconv"
	"os"
)

var scanner = bufio.NewScanner(os.Stdin)

func readInt() int {
	scanner.Scan()
	i, e := strconv.Atoi(scanner.Text())
	if e != nil {
		panic(e)
	}

	return i
}


func main() {
	scanner.Split(bufio.ScanWords)
	n := readInt()
	a_list := make([] int, 4 * n - 1)
	for i := 0; i < 4 * n - 1; i ++ {
		a_list[i] = readInt()
	}

	count_list := make([] int, n)

	for _, a := range(a_list) {
		count_list[a - 1] += 1
	}

	var ans int
	for i, count := range(count_list) {
		if count == 3 {
			ans = i + 1
			break
		}
	}

	fmt.Println(ans)
}

