

package main

import "bufio"
import "fmt"
import "os"
import "strconv"


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
	B := make([] int, 200)
	for i := 0; i < n; i ++ {
		x := A[i] % 200
		B[x] += 1
	}
	fmt.Println(B)
	memo := -1
	for i := 0; i < 200; i ++ {
		if B[i] >= 2 {
			memo = i
			fmt.Println("Yes")
		}
	}
	memo2 := 0
	for i := 0; i < n; i ++ {

		if A[i] % 200 == memo && memo2 < 2{
			memo2 += 1
			fmt.Println(1, i + 1)
			if memo2 == 2 {
				os.Exit(0)
			}
		}
	}

	dp := make([][] int, n)
	for i := 0; i < n; i ++ {
		dp[i] = make([] int, n)
	}

	for i := 0; i < n; i ++ {
		dp[0][i] = A[i] % 200
	}

	for i := 1; i < n; i ++ {
		for j := 0; j < n; j ++ {
			if i == j{
				dp[i][j] = dp[i - 1][j]
			} else {
				dp[i][j] = (dp[i - 1][j] + A[j]) % 200
			}
		}
	}
	memo4 := make([] int, 200)





	for i := 0; i < n; i ++ {
		for j := 0; j < n; j ++ {
			memo4[dp[i][j]] += 1
			if memo4[dp[i][j]] == 2 {
				y := dp[i][j]
				for k := 0; k < n; k ++ {
					for r := 0; r < n; r ++ {
						if dp[k][r] == y {
							ans := make([] int)
						}
					}
				}
			}
		}
	}



}