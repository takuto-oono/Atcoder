package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
	"sort"
)

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
    sc.Scan()
    i, e := strconv.Atoi(sc.Text())
    if e != nil {
        panic(e)
    }
    return i
}

func main() {
	sc.Split(bufio.ScanWords)
	var n int
	n = nextInt()
	A := make([] int, n)
	B := make([] int, n)
	for i := 0; i < n; i ++ {
		A[i] = nextInt()
	}
	for i := 0; i < n; i ++ {
		B[i] = nextInt()
	}

	C := make([] int, n)
	for i := 0; i < n; i ++ {
		C[i] = A[i] - B[i]
	}

	sort.Sort(sort.IntSlice(C))
	

	ans := 0
	accumulation := 0

	for i := 0; i < n; i ++ {
		if C[i] >= 0 {
			break
		} else {
			ans += 1
			accumulation -= C[i]
			
		}
	}

	for i := 0; i < n; i ++ {
		index := n - 1 - i
		if C[index] <= 0 || accumulation <= 0 {
			break
		} else {
			ans += 1
			accumulation -= C[index]
			
		}
	}

	if accumulation > 0 {
		ans = -1
	}
	fmt.Println(ans)



}