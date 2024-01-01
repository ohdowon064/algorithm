package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	b2 := b
	for i := 1; i <= 3; i++ {
		fmt.Println(a * (b % 10))
		b /= 10
	}
	fmt.Println(a * b2)
}
