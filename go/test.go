package main

import (
	"fmt"
)

func main(){
	var y int
	y = 10
	var x string = "Hello W!"
	//var name string
	//fmt.Scanf("Enter your name: %s", &name)
	fmt.Println(x == string(y))
	fmt.Println(`1 2 3 4`)
	i := 1
	for i=0; i < 10; i++{
		switch i{
		case 5:
			fmt.Println("Prints 5")
		default:
			fmt.Println(i)
		}

	}
	
	myMap := make(map[int]string)
	myMap[4] = "Nava"
	fmt.Println(myMap)
	
}
