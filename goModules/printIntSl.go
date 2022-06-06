package main

import (
	"fmt"
	"strconv"
	"strings"
)

func printIntSlice(sl []int) {
	ans := []string{}
	for _, v := range sl {
		ans = append(ans, strconv.Itoa(v))
	}
	fmt.Println(strings.Join(ans, " "))
}
