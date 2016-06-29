package main

import "fmt"
import "math"

const s = "Nava"


func main(){
	fmt.Println(s)

	const n = 10000
	const b = n/2.0
	fmt.Println(int32(b))
	fmt.Println(math.Sin(n))
}
