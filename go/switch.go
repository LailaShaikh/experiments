package main

import "fmt"
import "time"

func main(){

	switch n:= 10; n%2 {
	case 1:
		fmt.Println("Odd dude!")
	default:
		fmt.Println("Even dude!")
	}

	fmt.Println(time.Now().Weekday())
	switch time.Now().Weekday() {
	case time.Saturday, time.Sunday:
		fmt.Println("Week End Dude! :) ")
	default:
		fmt.Println(" Week day :(")
	}

	t := time.Now()
	switch t.Hour() {
	case 17:
		fmt.Println(t.Hour())
	default:
		fmt.Println("Default",t.Hour())
	}
}
