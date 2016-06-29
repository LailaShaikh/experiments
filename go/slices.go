package main

import "fmt"

func main(){
	a := make([]string, 3)
	a[0] = "3"
	a = append(a, "Nava", "e", "f", "g")
	fmt.Println("A is:", a)

	// copy an array
	c := make([]string, len(a))
	copy(c, a)
	fmt.Println("copied:", c)

	twoD := make([][]int, 5)
	for i:=0; i<5; i++ {
		twoD[i] = make([]int, i+1)
		for j:=0; j<i+1; j++ {
			twoD[i][j] = i+j
		}
	}
	fmt.Println("my 2d is:", twoD)
}


