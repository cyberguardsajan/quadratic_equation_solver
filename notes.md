
### **Key Concepts and Steps:**

1. **Importing Math Module:**
   - The `math` module is imported to use the `sqrt()` function, which computes the square root.

   ```python
   import math
   ```

2. **Input Values:**
   - The program prompts the user to input the values of `a`, `b`, and `c` (which are coefficients of the quadratic equation).
   - These inputs are converted to `float` to ensure that the program handles decimal values.
   
3. **Discriminant Calculation:**
   - The discriminant `Δ` determines the nature of the roots.
   - It is calculated as:
   
   ```python
   Δ = b^2 - 4ac
   ```

4. **Checking the Discriminant (Delta):**
   - The program uses conditional statements to check the value of the discriminant.
   
   #### **Case 1: Two Real and Distinct Solutions (`Δ > 0`)**
   - When the discriminant is positive, the quadratic equation has two real and distinct solutions:
   
   ```python
   x1 = (-b + sqrt(Δ)) / (2a)
   x2 = (-b - sqrt(Δ)) / (2a)
   ```

   ```python
   if discrim > 0:
       print((-b + math.sqrt(discrim)) / (2 * a))
       print((-b - math.sqrt(discrim)) / (2 * a))
   ```

   #### **Case 2: One Real Solution (`Δ = 0`)**
   - If the discriminant is zero, the quadratic equation has exactly one real solution (a repeated root):
   
   ```python
   x = -b / 2a
   ```

   ```python
   elif discrim == 0:
       print(-b / (2 * a))
   ```

   #### **Case 3: No Real Solutions (`Δ < 0`)**
   - If the discriminant is negative, the quadratic equation has no real solutions (the solutions are complex).
   
   ```python
   else:
       print("No real solutions for this equation.")
   ```
```
