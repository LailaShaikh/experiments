package main

import (
	"fmt"
	"time"
)

func Runner(x chan int){
	runner_no :=  <-x
	fmt.Println("Runner No:", runner_no)
	
	if runner_no == 4{
		fmt.Println("Race is done..bye bye..")
		return 
	}else {
		go Runner(x)
		time.Sleep(time.Microsecond * 10)
	}
	
	x <- runner_no + 1
	time.Sleep(time.Microsecond * 5)
}

func main(){
	fmt.Println("Baton Relay starts")
	baton := make(chan int)
	
	go Runner(baton)
	baton <- 1
	time.Sleep(500 * time.Millisecond)
}
