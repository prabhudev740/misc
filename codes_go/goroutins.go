package main

import (
	"fmt"
	"sync"
)

var count int

func main() {
	wg := sync.WaitGroup{}
	mu := sync.Mutex{}

	for i := 0; i < 500; i++ {
		wg.Add(1)
		go func() {
			mu.Lock()
			increment()
			wg.Done()
			mu.Unlock()
		}()
		wg.Wait()
	}

	// go increment()
	// time.Sleep(10 * time.Nanosecond)
	fmt.Println(count)
}

func increment() {
	count++
}
