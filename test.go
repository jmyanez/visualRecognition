package main
import "fmt"
import "os/exec"

func main() {
    cmd := exec.Command("python", "./print.py")

    out, err := cmd.CombinedOutput()
    if err != nil { fmt.Println(err); }
    fmt.Println(string(out))
}
