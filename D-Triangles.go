package main
import "fmt"
import "sort"
func main() {
	var n, ans int
	fmt.Scan(&n)
	L := make([] int, n)
	for i := 0; i < n; i ++ {
		fmt.Scan(&L[i])
	}
	sort.Sort(sort.IntSlice(L))
	ans = 0
	for i := 0; i < n - 2; i ++ {
		for j := i + 1; j < n - 1; j ++ {
			for k := j + 1; k < n; k ++ {
				a, b, c := L[i], L[j], L[k]
				if c < a + b {
					ans += 1
				}
			}
		}
	}
	fmt.Println(ans)
}