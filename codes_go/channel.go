package main

import (
	"fmt"
	"time"
)

func main() {
	c := make(chan string)

	go gopher(c)
	for {
		v, open := <-c
		if !open {
			break
		}
		fmt.Println(v)
	}
}

func gopher(c chan string) {
	for i := 0; i < 5; i++ {
		c <- "gopher"
		time.Sleep(500 * time.Millisecond)
	}
	close(c)
}
