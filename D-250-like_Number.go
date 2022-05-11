package main

import (
	"bufio"
	"fmt"
	"math"
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

func createPrimeSlice(n int) []bool {
	isPrimeSlice := []bool{}
	for i := 0; i < n+1; i++ {
		isPrimeSlice = append(isPrimeSlice, true)
	}
	isPrimeSlice[0], isPrimeSlice[1] = false, false
	for i := 2; i < n+1; i++ {
		if i*i > n {
			break
		}
		if isPrimeSlice[i] {
			for j := 2 * i; j < n+1; j += i {
				isPrimeSlice[j] = false
			}
		}
	}
	return isPrimeSlice
}

func remove(sl []int, index int) []int {
	return sl[:index+copy(sl[index:], sl[index+1:])]
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

func sqrt(n, m int) int {
	ans := 1
	for i := 1; i < n+1; i++ {
		if pow(i+1, m) > n {
			break
		}
		ans = i
	}
	return ans
}

func pow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}

func main() {
	n := intInput()
	ans := 0
	lim := sqrt(n, 3) + 1
	primeSlice := createPrimeSlice(lim)

	for q := 2; q < lim+1; q++ {
		if !primeSlice[q] {
			continue
		}
		q3 := q * q * q
		for p := 2; p < lim+1; p++ {
			if p >= q {
				break
			}

			if p*q3 > n {
				break
			}
			if !primeSlice[p] {
				continue
			}
			if p*q3 <= n && p < q {
				ans += 1
			}
		}
	}
	fmt.Println(ans)
}
