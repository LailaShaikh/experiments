package main

import "fmt"

func point(j *int){
	*j = 10
}

func main(){
	i := 4
	fmt.Println("Initial: ", i)
	point(&i)
	fmt.Println("Modified: ", i)
}

