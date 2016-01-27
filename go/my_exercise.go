package main

import (
	"fmt"
	"math/rand"
	"sort"
)

type Mapian struct {
	Name string
	Friends map[string]*Mapian
}


func add(b int, a int) int {
	return a + b
}

func MapExercise(){
	mymap := make(map[string]int)
	mymap["nava"] = 9
	fmt.Println("My Initial Map is", mymap)
	power, exists := mymap["test"]
	fmt.Println(power, exists, len(mymap))
	delete(mymap, "deletekeyhere")
	for k,v := range mymap {
		fmt.Println(k,v)
	}
	mapian := &Mapian{ Name: "Gokul", Friends: make(map[string]*Mapian) }
	mapian.Friends["Test"] = &Mapian{Name: "Anand"}
	fmt.Println(mapian.Friends["Test"])
}

func arrTest(){
	ta := make([]int, 0, 20)
	ta = append(ta, 4)
	ta = append(ta, 5)
	for v := 0; v < 10; v++{
		ta = append(ta, v)
		fmt.Println(ta)
	}
	tan := ta[3:6]
	tan[0] = 11
	fmt.Println(tan, ta)
	for i:=0; i<20; i++{
		ta = append(ta, int(rand.Int31n(1000)))
	}
	sort.Ints(ta)

	dest := make([]int, 20)
	copy(dest, ta)
	fmt.Println("Dest:=",dest, len(ta))

	MapExercise()
}


/*
func extrPow(sai []*SG) []int{
	pow := make([]int, len(sai))
	for index, saaa := range sai{
		pow[index] = saaa.Power
	}
	return pow
}
*/

func arrayExample() {
	arr := make([]int, 0, 10)
	arr = append(arr, 5)
	fmt.Println("Curr Arr is", arr)
	intC := cap(arr)
	fmt.Println("Intial Capacity is", intC)
	for i := 0; i<40; i++ {
		arr = append(arr, i)
		if intC != cap(arr){
			//fmt.Println("Curr Cap", cap(arr))
		}
	}
	fmt.Println("Final Cap is", cap(arr))
}

func main(){
	s := make([]int, 5, 10);
	fmt.Println("Exerise Test", add(4, 5));
	s = append(s, 22);
	fmt.Println("Intial Array", s)
	arrayExample()
	arrTest()
}
