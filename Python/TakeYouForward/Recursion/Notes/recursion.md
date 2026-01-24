# Recursion

- When a fucntion call itself that property is called Recursion.

```
printFucntion(){
    printFucntion()
}
```

- It will into a infinite loop

- We need to stop it using a finite recursion using base condition.

```
func() {
    base condition

    // to-do statments. Actual logic 

}
```

## Tail Recursion

***Def*** - First do your job and then call the function

Example: Print your name 4 times

```
cnt = 0 --> global variable
func(){
    if cnt == 4:
       return 
    print("Babu")
    cnt += 1
    func()
}
```

## Head Recursion

***Def*** - Do the job when the fucntion returns. Its also known as Backtracing.


```
cnt = 0
func(){
    if cnt == 4:
    return 
    
    cnt += 1
    func()
    print("Babu)
}
```

## Stack overflow

***Def*** - When the fucntion does not end calling itself is stack overflow. Memory will get overflow.

## Time complexity Analysis:

- There is no loop is running in Recursion. 
- Tc: O(N)
- Sc: O(N) --> It because of the Stack memory

## II.Recursion Concepts:

- ***Importtant*** - Base condition is Important

