package main

import "bufio"
import "fmt"
import "os"
import "strconv"
import "sort"

var sc = bufio.NewScanner(os.Stdin)

func nextInt() int {
	sc.Scan()
	i, e := strconv.Atoi(sc.Text())
	if e != nil {
		panic(e)
	}
	return i
}

func main(){
	sc.Split(bufio.ScanWords)
	n := nextInt()
	A := make([] int, n)
	for i := 0; i < n; i ++ {
		A[i] = nextInt()
	}
	sort.Sort(sort.IntSlice(A))
	ans := 0
	dp := make([] int, 200)
	for i := 0; i < n; i ++ {
		x := A[i] % 200
		dp[x] += 1
	}
	for i := 0; i < 200; i ++ {
		if dp[i] >= 2 {
			ans += dp[i] * (dp[i] - 1) / 2
		}
	}




	fmt.Println(ans)



}