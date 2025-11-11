# edit-distance
Homework BIL-377 lesson

Отлично — вот полностью оформленный **готовый шаблон репозитория**, в стиле ссылок твоих одногруппников. Просто копируй и вставляй в GitHub. Все выглядит максимально похоже по структуре и оформлению.

---




## Edit Distance (Levenshtein) — Dynamic Programming

### 📌 Description

This project implements the Edit Distance (Levenshtein Distance) algorithm using **Dynamic Programming**.
The algorithm calculates the minimum number of operations required to transform one string into another.

Allowed operations:

* insertion
* deletion
* substitution

The method is widely used in NLP, search engines, spell-checking mechanisms and bioinformatics.

---

## 📎 Algorithm Explanation

We define:

```
dp[i][j] = minimum number of operations to convert a[:i] into b[:j]
```

To fill the DP table:

* dp[0][j] = j (insert j characters)
* dp[i][0] = i (delete i characters)

For each pair of characters a[i-1] and b[j-1]:

```
if a[i-1] == b[j-1]:
    cost = 0
else:
    cost = 1
```

Choose minimum of:

* deletion      → dp[i-1][j] + 1
* insertion     → dp[i][j-1] + 1
* substitution  → dp[i-1][j-1] + cost

Final answer: `dp[n][m]`

---

## 🧩 Algorithm Steps

1. Create a DP table (n+1)×(m+1)
2. Initialize first row and first column
3. Fill the table using the recurrence rule
4. The value at dp[n][m] is the Edit Distance
5. (Optional) Reconstruct operations path

---

## ✅ Python Implementation

```python
def edit_distance(a: str, b: str) -> int:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # fill the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )
    return dp[n][m]


# example
print(edit_distance("kitten", "sitting"))
```

---

## 💡 Example

Input:

```
kitten
sitting
```

Output:

```
3
```

Explanation:

1. kitten → sitten   (replace k→s)
2. sitten → sittin   (replace e→i)
3. sittin → sitting  (insert g)

---

## 📘 Visualization Example (matrix)

```
    '' s i t t i n g
''  0 1 2 3 4 5 6 7
k   1 1 2 3 4 5 6 7
i   2 2 1 2 3 4 5 6
t   3 3 2 1 2 3 4 5
t   4 4 3 2 1 2 3 4
e   5 5 4 3 2 2 3 4
n   6 6 5 4 3 3 2 3
```

---

## 🔍 Applications

### ✅ NLP / Text Processing

* spell checking
* autocorrection
* fuzzy search
* similarity scoring
* search engines (“did you mean?”)

### ✅ Bioinformatics

* DNA/RNA sequence comparison
* protein analysis

### ✅ Machine Learning

* preprocessing text
* clustering string datasets

---

## ✅ Conclusion

Edit Distance is a fundamental dynamic programming technique that:

* is simple and intuitive
* handles approximate text comparison effectively
* is widely used in modern software systems
* has clean and clear DP logic
* runs in O(n × m) time

This project provides a clean and ready-to-use implementation, following classic dynamic programming structure.

---



```
# Edit Distance Algorithm — Presentation

## What is Edit Distance?
A metric for comparing two strings by counting the minimum number of required operations.

## Why is it useful?
- spell checking
- text normalization
- DNA/RNA sequence comparison
- fuzzy search
- NLP pipelines

## Algorithm Steps
1. Build DP table (n+1 × m+1)
2. Initialize row and column
3. Fill table using min(insertion, deletion, substitution)
4. Final result at dp[n][m]

## Complexity
Time: O(n*m)  
Space: O(n*m)

## Example
kitten → sitting  
distance = 3

## Conclusion
Edit Distance is a powerful and widely used algorithm for string similarity.
```

---

