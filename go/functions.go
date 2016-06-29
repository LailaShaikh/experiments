package main

import "fmt"

func add(a, b int) (int, float32) {
	return a+b, 0.31
}

func main(){
	res, _ := add(5, 4)
	fmt.Println("Result: ", res)
}
