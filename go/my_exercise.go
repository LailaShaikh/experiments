package main

import "fmt"

func add(b int, a int) int {
	return a + b
}

func arrayExample() {
	arr := make([]int, 0, 10)
	arr = append(arr, 5)
	fmt.Println("Curr Arr is", arr)
	intC := cap(arr)
	fmt.Println("Intial Capacity is", intC)
	for i := 0; i<40; i++ {
		arr = append(arr, i)
		if intC != cap(arr){
			fmt.Println("Curr Cap", cap(arr))
		}
	}
	fmt.Println("Final Cap is", cap(arr))
}

func main(){
	s := make([]int, 5, 10);
	fmt.Println("Exerise Test", add(4, 5));
	s = append(s, 22);
	fmt.Println("Intial Array", s)
	arrayExample()
}
