package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var rdr = bufio.NewReaderSize(os.Stdin, 1000000)

func stringInput() string {
	sc.Scan()
	return sc.Text()
}

func intInput() int {
	sc.Scan()
	x, err := strconv.Atoi(sc.Text())
	if err != nil {
		panic(err)
	}
	return x
}

func largeInput() string {
	buf := make([]byte, 0, 1000000)
	for {
		l, p, err := rdr.ReadLine()
		if err != nil {
			panic(err)
		}
		buf = append(buf, l...)
		if !p {
			break
		}
	}
	return string(buf)
}

func intSliceInput(n int) []int {
	sl := []int{}
	for i := 0; i < n; i++ {
		x := intInput()
		sl = append(sl, x)
	}
	return sl
}

func init() {
	sc.Split(bufio.ScanWords)
}

func createPrimeSl(n int) []int {
	numMap := map[int]bool{}
	for i := 2; i < n+1; i++ {
		numMap[i] = true
	}
	for i := 2; i < n+1; i++ {
		if numMap[i] {
			for j := 2 * i; j < n+1; j += i {
				numMap[j] = false
			}
		}
	}
	primeSl := []int{}
	for k, f := range numMap {
		if f {
			primeSl = append(primeSl, k)
		}
	}
	return primeSl

}

func isPrime(n int) bool {
	for i := 2; i < n+1; i++ {
		if i*i > n {
			break
		}
		if n%i == 0 {
			return false
		}
	}
	return true
}

func factorization(n, lim int, primeSl []int) int {
	tmp := n
	ans := 1
	for _, prime := range primeSl {
		if tmp == 1 {
			break
		}
		if tmp%prime == 0 {
			cnt := 0
			memo := prime
			cnt2 := 0
			for tmp%prime == 0 {
				tmp /= prime
				memo *= prime
				if memo > lim {
					cnt2 += 1
				}
				cnt += 1
			}
			ans *= cnt + 1 - 2*cnt2
		}
	}
	return ans
}

func divisor(n int, primeSl []int) []int {
	divisorSlice := []int{}
	for _, i := range primeSl {
		if i*i > n {
			break
		}
		if n%i == 0 {
			divisorSlice = append(divisorSlice, i)
			if i*i != n {
				divisorSlice = append(divisorSlice, n/i)
			}
		}
	}
	return divisorSlice
}

func check(sl []int) bool {
	for _, v := range sl {
		if !isPrime(v) {
			return false
		}
	}
	return true
}

func main() {
	n := intInput()
	primeSl := createPrimeSl(n)
	primeSl = append(primeSl, 1)
	ans := 0
	for i := 1; i < n+1; i++ {
		v := i * i
		dSl := divisor(v, primeSl)
		for _, d := range dSl {
			if d <= n && v/d <= n {
				ans += 1
			}
		}
	}
	fmt.Println(ans)
}
