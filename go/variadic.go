package main

import "fmt"

func varia(nums ...int) int {
	fmt.Println("nums:", nums)
	for i, v := range nums {
		fmt.Println("i, v", i, v)
	}
	return 1
}

func main(){
	_ = varia(1, 2, 3, 4, 5)
	arr := []int{6, 7, 8, 9, 9}
	
	_ = varia(arr...)
}
