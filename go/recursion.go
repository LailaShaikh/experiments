package main

import "fmt"

func recr(i int) int {
	if i == 0{
		return 1
	}
	return i * recr(i-1)
}

func main(){
	resu := recr(6)
	fmt.Println("The factorial of 6 is:", resu)
}
