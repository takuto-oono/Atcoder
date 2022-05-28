package main

import (
	"fmt"
)

func main() {
    sl := []int{0, 1}
    for _, v := range sl {
        fmt.Println(sl)
        if v == 1 {
            sl = append(sl, 2)    
        }
    }
}
