// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// The package name is expected by the test program.
package hello
// It has to stay just the way it is.

import "fmt"

// testVersion identifies the version of the test program that you are
// writing your code to. If the test program changes in the future --
// after you have posted this code to the Exercism site -- nitpickers
// will see that your code can't necessarily be expected to pass the
// current test suite because it was written to an earlier test version.
const testVersion = 2

// It's good style to write a comment here documenting HelloWorld.
// (But delete all these instructional comments!)
func HelloWorld(name string) string {
	if name == "" {
		name = "World"
	}
	return fmt.Sprintf("Hello, %s!", name)
}
