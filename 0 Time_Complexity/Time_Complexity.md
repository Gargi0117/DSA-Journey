# ⏱ Time Complexity

Understanding **time complexity** is the foundation of Data Structures and Algorithms.  
It helps us analyze how the runtime of an algorithm grows as the input size increases.

Instead of measuring actual execution time, we analyze the **rate of growth**.

---

# 📊 Why Time Complexity Matters

When solving problems, there are often multiple approaches.

Example:

- One solution may take **10 seconds**
- Another may take **0.01 seconds**

As the input grows, inefficient algorithms become **impractical**.

Time complexity helps us choose the **most scalable solution**.

---

# 📈 Big O Notation

**Big O notation** describes the **upper bound** of an algorithm's runtime.

It answers the question:

> How does the algorithm perform in the **worst case** as input size grows?

Example:

```
O(1)      → Constant Time
O(log n)  → Logarithmic Time
O(n)      → Linear Time
O(n log n)→ Linearithmic Time
O(n²)     → Quadratic Time
```

---

# 📉 Common Time Complexities

| Complexity | Name | Example |
|------------|------|--------|
| **O(1)** | Constant | Accessing array element |
| **O(log n)** | Logarithmic | Binary Search |
| **O(n)** | Linear | Traversing an array |
| **O(n log n)** | Linearithmic | Merge Sort |
| **O(n²)** | Quadratic | Nested loops |
| **O(2ⁿ)** | Exponential | Recursive Fibonacci |

---

# 📊 Complexity Comparison

```
Best → Worst
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
```

As the input grows large:

- **O(1)** stays constant
- **O(n²)** becomes extremely slow

---

# 🧠 Example

### Linear Search

```python
def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True
    return False
```

**Time Complexity**

```
O(n)
```

Because in the worst case we must check every element.

---

# ⚡ Example

### Binary Search

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
```

**Time Complexity**

```
O(log n)
```

Because the search space is halved every step.

---

# 🎯 Key Takeaways

- Time complexity measures **growth of runtime**
- It helps compare **different algorithms**
- Lower complexity → **better scalability**
- Important for **technical interviews and real systems**

---

# 📚 Next Steps

After understanding time complexity, the next step is learning:

- Arrays
- Strings
- Linked Lists
- Trees
- Graphs

These data structures form the building blocks for algorithm design.

---

⭐ If you find this repository helpful, consider giving it a star!