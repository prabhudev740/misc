package main

import "fmt"

func main() {
	fmt.Println(getConcatenation([]int{1, 2, 1}))
	fmt.Println(getConcatenation([]int{1, 3, 2, 1}))
}

func getConcatenation(nums []int) []int {
	n := len(nums)
	x := make([]int, n*2)

	for i, v := range nums {
		x[i], x[i+n] = v, v
	}
	return x
}
