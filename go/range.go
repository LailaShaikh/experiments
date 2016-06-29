package main

import "fmt"

func main(){
	k := map[int]int {0:0, 1:1, 2:2}
	fmt.Println(k)

	for k,v := range k {
		fmt.Println("K:",k, "V:", v)
	}
	
	for i,c := range "navaneethan"{
		fmt.Printf("%s->%s\n", i, c)
	}
}
