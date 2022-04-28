package main

import "fmt"

func calCumulativeSum(sString string) []int {
	cumulativeSumList := make([]int, len(sString)+1)
	cnt := 0
	for i, s := range sString {
		if string(s) == "." {
			cnt += 1
		}
		cumulativeSumList[i + 1] = cnt
	}
	return cumulativeSumList
}

func main() {
	var sString string
	var k int
	fmt.Scan(&sString)
	fmt.Scan(&k)
	fmt.Println(k)
	calCumulativeSum(sString)
	cumulativeSumList := calCumulativeSum(sString)
	ans, right := 0, 0
	for left := 0; left < len(sString); left ++ {
		for {
			if (right >= len(sString)) && (cumulativeSumList[right + 1] - cumulativeSumList[left] <= k) {
				right ++
			}
			else

		}
	}

}
