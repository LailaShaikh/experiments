package main

import "fmt"

func clos() func() int {
	i := 3
	return func() int {
		i += 1
		return i
	}
}

func main(){
	nes_fun := clos()
	fmt.Println(nes_fun())
	fmt.Println(nes_fun())
	fmt.Println(nes_fun())
	fmt.Println(nes_fun())
	nes_fun = clos()	
	fmt.Println(nes_fun())
	
}
