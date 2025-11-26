# DSA Topic:

## Array:

- Collections of elememts 
- Elements are homegeneous (Same data type)
- Arranged in a contagious pattern (Immediately the next elements will start)
- In Python Lists we can store hetrogeneous elements too! 

***arr[index] = base address + index * sizeof(datatype)***
- arr[3] = 200 + 3 * 4 = 212

## Advantages of Contagious mem allocation:

- Reduces redundancy
- Random access in O(1)

## Disadantages:

1. Homegeneous data
2. Fixed size
3. External Fragmentation(rare and solvable)

## Dynamic Array:

1. Size is not fixed and other properties are same
2. In python it is called 'List'
3. In C++ call ed vector
4. In Java its called arrayList

## Interview questions:

## BIO OH Means Worst case

1. What is the worst case time complexity in a static array? 
Ans: O(1)

2. What is the worst case TC updating N elements in a static array?
Ans: O(N)

3. What is the worst case TC updating an element in dynamic array? 
Ans: O(N)

4. What is the worst case TC updating N elements in a dynamic array?
Ans: O(N^2)