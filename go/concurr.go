package main

import (
	"fmt"
	"time"
	"sync"
)

var (
	counter = 0
	lock sync.Mutex
)

func main(){
	var numSlice = []int{1,2,3}
	fmt.Println("Hai", numSlice)
	for i:=0; i<10; i++ {
		go incr()
	}
	time.Sleep(time.Millisecond * 10)
}

func incr(){
	lock.Lock()
	defer lock.Unlock()
	counter ++
	fmt.Println(counter)
}
