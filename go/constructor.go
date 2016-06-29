package main

import (
	"fmt"
	
)

type Work struct {
	tech string
	rating int
	level string
}

func (tw *Work) getAdvanced() {
	fmt.Println("Checking Advanced or Not?")
	n := new(Work)
	n.tech = "go"
	n.rating = 3
	n.level = "beginner"
	//return n
}

type Work2 struct {
	*Work
	sequence int

}

func main() {
	fmt.Println("Started")
	w := &Work{tech:"Python", rating:8, level:"Advanced"}
	fmt.Println("Work Tech:", w)
	w.getAdvanced()
	//fmt.Println("Return of getAdvanced", c)

	w2 := &Work2{Work: &Work{tech:"go", rating:4, level:"Starter"}, sequence:2}
	fmt.Println("Work2 Struct", w2, w2.tech)

	//Arrays
	score := make([]int, 0, 7)
	score = append(score, 990)
	c := cap(score)
	fmt.Println("Score is", score[0], append(score, 99), c)

	for i := 0; i < 25; i++{
		score = append(score, i)
		if cap(score) != c {
			c = cap(score)
			fmt.Println("Cap:",c)
		}
	}
}


