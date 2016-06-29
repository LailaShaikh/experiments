package main

import "fmt"

func main(){
	mymap := make(map[string]int)
	mymap["name"] = 1
	mymap["age"] = 0
	fmt.Println("Mymap:", mymap)
	fmt.Println("Get", mymap["name"])
	delete(mymap, "name")
	k1, k2 := mymap["name"]
	fmt.Println(k1, k2)
}
