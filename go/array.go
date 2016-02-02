package main

import (
	"fmt"
)

func main(){
	fmt.Println("Arrays")
	s := []int{6,6,6}
	s1 := make([]int, 5, len(s)+5)
	s2 := s1[:]
	s1 = append(s1, s...)
	fmt.Println("Slice S1:", s1, s2)
	copy(s2, s1[2:len(s1)])
	fmt.Println("After copy", s2)
}
