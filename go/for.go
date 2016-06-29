package main

import "fmt"

func main(){
	i := 1
	for i <= 7 {
		fmt.Println(i)
		i = i + 1
	}

	for j:=0; j<5; j++ {
		fmt.Println("Jii",j)
	} 

	for {
		fmt.Println("Infini.")
		break
	}
}
