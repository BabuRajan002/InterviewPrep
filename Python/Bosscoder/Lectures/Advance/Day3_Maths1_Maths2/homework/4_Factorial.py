class Factorial:
    def __init__(self,n):
         self.n = n
    
    def solve(self):
        # Brute force solution
        #  n = self.n
        #  number = 1 
        #  for i in range(1, n+1):
        #       number *= i
        #  count = 0
        #  prevDigit = 0
        #  while number > 0:
        #       currDigit = number % 10
        #       if currDigit == 0 and prevDigit == 0:
        #            count += 1
        #            prevDigit = currDigit
        #       elif currDigit !=0 or prevDigit != 0:
        #            break
        #       number //= 10     
         count = 0
         n = self.n 
         while n > 0:
              n //= 5
              count += n              
         return count
if __name__ == "__main__":
     fact = Factorial(7)
     print(fact.solve())

#Notes Behind this solution: 

# Perfect 👍
# Below is a **complete, math-only note**, exactly in the style you can **print or hand-write**, plus a **worked example** and a **30-second interview explanation**.

# ---

# # 📘 Trailing Zeroes in `n!` — Math Logic & Intuition

# ---

# ## 1. What creates a trailing zero?

# A trailing zero means the number is divisible by **10**.

# [
# 10 = 2 \times 5
# ]

# 👉 **Each trailing zero requires one pair of (2, 5)** in the prime factorization.

# ---

# ## 2. Prime factorization of `n!`

# [
# n! = 1 \times 2 \times 3 \times \cdots \times n
# ]

# This product contains many prime factors, especially **2s** and **5s**.

# ---

# ## 3. Why factors of 2 are abundant

# * Every even number contributes at least one factor of **2**
# * Numbers like (4, 8, 16) contribute **multiple 2s**

# [
# \text{Number of 2s in } n! \gg \text{Number of 5s}
# ]

# ✔️ So **2 is never the limiting factor**

# ---

# ## 4. Why factors of 5 decide the answer

# * Only numbers divisible by **5** contribute a factor of 5
# * Multiples of 5 are comparatively rare

# Since each trailing zero needs **one 2 and one 5**, and **2s are plenty**:

# [
# \boxed{\text{Trailing zeros in } n! = \text{Number of factors of 5 in } n!}
# ]

# ---

# ## 5. Counting factors of 5 (important insight)

# Some numbers contribute **more than one 5**:

# * (5 = 5^1) → 1 factor of 5
# * (25 = 5^2) → 2 factors of 5
# * (125 = 5^3) → 3 factors of 5

# So we must count **all powers of 5**.

# ---

# ## 6. Mathematical formula

# [
# \boxed{
# \text{Trailing zeros in } n!
# ============================

# \left\lfloor \frac{n}{5} \right\rfloor
# +
# \left\lfloor \frac{n}{25} \right\rfloor
# +
# \left\lfloor \frac{n}{125} \right\rfloor

# * \cdots
#   }
#   ]

# (Stop when the division becomes zero.)

# ---

# # ✍️ Worked Example (Math-Only)

# ### Example: `n = 100`

# [
# \left\lfloor \frac{100}{5} \right\rfloor = 20
# ]
# [
# \left\lfloor \frac{100}{25} \right\rfloor = 4
# ]
# [
# \left\lfloor \frac{100}{125} \right\rfloor = 0
# ]

# [
# \boxed{20 + 4 = 24 \text{ trailing zeros}}
# ]

# ✔️ `100!` ends with **24 zeros**

# ---

# # 🎯 Key Intuition (One-Liner)

# > **Trailing zeros in `n!` depend on how many times 5 divides `n!`, because factors of 2 are always sufficient.**

# ---

# # 🧠 30-Second Interview Explanation

# > “A trailing zero comes from a factor of 10, which is 2 × 5.
# > In a factorial, there are far more factors of 2 than 5, so 2s are never the limiting factor.
# > Therefore, the number of trailing zeros in `n!` equals the number of times 5 appears in its prime factorization.
# > We count this using ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ and so on.”

# ---

# If you want next, I can:

# * Turn this into a **Markdown (.md) note** for your Linux / DSA notebook
# * Add a **common pitfalls section** (very useful for interviews)
# * Give a **1-line memory trick** you’ll never forget

# Just say 👍


