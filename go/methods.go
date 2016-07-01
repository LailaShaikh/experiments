package main

import "fmt"

type person struct {
	name string
	age int
}

func (p *person) print_details() string {
	fmt.Println(p.name, p.age)
	return p.name
}

func main(){
	s := person{name: "Navaneethan", age: 20}
	fmt.Println(s)
	fmt.Println(s.print_details())
}
