Below is the **complete List + String interview question set from your 180-question list**, with answers and examples. I’ll keep the answers **interview-friendly but detailed enough to understand the concept**.

# 🟢 PART 1 — PYTHON LIST QUESTIONS

## Q116. What is a list?

A **list** is an ordered, mutable collection used to store multiple values in a single variable.

```python
numbers = [10, 20, 30, 40]
```

Properties:

- Ordered
- Mutable
- Allows duplicates
- Can store different data types
- Dynamically sized

```python
data = [10, "Aayush", 20.5, True]
```

---

## Q117. Why are lists mutable?

**Mutable** means the object can be changed after creation.

```python
numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)
```

Output:

```text
[10, 200, 30]
```

The same list object is modified.

Lists are designed to support operations such as:

```python
append()
remove()
insert()
sort()
```

---

## Q118. How do you create a list?

Use square brackets `[]`.

```python
numbers = [10, 20, 30]
```

Empty list:

```python
numbers = []
```

Using `list()`:

```python
numbers = list()
```

From another iterable:

```python
numbers = list("ABC")
print(numbers)
```

Output:

```text
['A', 'B', 'C']
```

---

## Q119. What is indexing in lists?

**Indexing** means accessing an individual element using its position.

```python
numbers = [10, 20, 30, 40]
```

Index:

```text
10 → 0
20 → 1
30 → 2
40 → 3
```

Example:

```python
print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

Python uses **zero-based indexing**.

---

## Q120. What is negative indexing?

Negative indexing accesses elements from the **end of the list**.

```python
numbers = [10, 20, 30, 40]
```

```text
10   20   30   40
 ↑    ↑    ↑    ↑
-4   -3   -2   -1
```

```python
print(numbers[-1])
```

Output:

```text
40
```

```python
print(numbers[-2])
```

Output:

```text
30
```

---

## Q121. What is slicing?

Slicing extracts a portion of a sequence.

Syntax:

```python
list[start:stop:step]
```

Example:

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

Important:

> `start` is included, `stop` is excluded.

You can also use:

```python
numbers[:3]
```

```text
[10, 20, 30]
```

And:

```python
numbers[::2]
```

```text
[10, 30, 50]
```

---

# Q122. Difference between `append()` and `extend()`?

### `append()`

Adds **one object** at the end.

```python
a = [1, 2]

a.append([3, 4])

print(a)
```

Output:

```text
[1, 2, [3, 4]]
```

### `extend()`

Adds elements from an iterable individually.

```python
a = [1, 2]

a.extend([3, 4])

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

### Easy memory trick

```text
append() → one item
extend() → multiple elements
```

---

# Q123. Difference between `append()` and `insert()`?

### `append()`

Adds at the end.

```python
a = [10, 20]

a.append(30)

print(a)
```

```text
[10, 20, 30]
```

### `insert()`

Adds at a specific index.

```python
a = [10, 20]

a.insert(1, 30)

print(a)
```

Output:

```text
[10, 30, 20]
```

Syntax:

```python
list.insert(index, value)
```

---

# Q124. Difference between `remove()` and `pop()`?

### `remove()`

Removes an element **by value**.

```python
a = [10, 20, 30]

a.remove(20)

print(a)
```

Output:

```text
[10, 30]
```

### `pop()`

Removes an element **by index** and returns it.

```python
a = [10, 20, 30]

x = a.pop(1)

print(x)
print(a)
```

Output:

```text
20
[10, 30]
```

If no index is provided:

```python
a.pop()
```

removes the last element.

---

# Q125. What does `clear()` do?

`clear()` removes all elements from a list.

```python
a = [10, 20, 30]

a.clear()

print(a)
```

Output:

```text
[]
```

The list itself remains available; its contents are removed.

---

# Q126. What does `copy()` do?

`copy()` creates a **shallow copy** of a list.

```python
a = [10, 20, 30]

b = a.copy()

print(b)
```

Output:

```text
[10, 20, 30]
```

Now:

```python
b.append(40)

print(a)
print(b)
```

Output:

```text
[10, 20, 30]
[10, 20, 30, 40]
```

`a` and `b` are different list objects.

---

# Q127. Difference between `sort()` and `sorted()`?

### `sort()`

Changes the original list.

```python
a = [30, 10, 20]

a.sort()

print(a)
```

Output:

```text
[10, 20, 30]
```

It returns `None`.

### `sorted()`

Creates and returns a new sorted list.

```python
a = [30, 10, 20]

b = sorted(a)

print(a)
print(b)
```

Output:

```text
[30, 10, 20]
[10, 20, 30]
```

### Remember:

```text
sort()   → modifies original list
sorted() → returns new sorted list
```

---

# Q128. Difference between `reverse()` and `reversed()`?

### `reverse()`

Modifies the original list.

```python
a = [1, 2, 3]

a.reverse()

print(a)
```

Output:

```text
[3, 2, 1]
```

### `reversed()`

Returns an iterator that goes through the list in reverse order.

```python
a = [1, 2, 3]

b = reversed(a)

print(list(b))
```

Output:

```text
[3, 2, 1]
```

---

# Q129. How do you find list length?

Use `len()`.

```python
a = [10, 20, 30, 40]

print(len(a))
```

Output:

```text
4
```

---

# Q130. How do you find max and min values?

Use `max()` and `min()`.

```python
numbers = [10, 50, 20, 40]

print(max(numbers))
print(min(numbers))
```

Output:

```text
50
10
```

---

# Q131. How do you count occurrences?

Use `count()`.

```python
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```

Output:

```text
3
```

---

# Q132. How do you merge two lists?

Several approaches exist.

### Using `+`

```python
a = [1, 2]
b = [3, 4]

c = a + b

print(c)
```

Output:

```text
[1, 2, 3, 4]
```

### Using `extend()`

```python
a.extend(b)
```

### Using unpacking

```python
c = [*a, *b]
```

---

# Q133. How do you remove duplicates?

One common approach is using `set()`:

```python
a = [10, 20, 10, 30, 20]

b = list(set(a))

print(b)
```

However, this does **not guarantee the original order** in the general case.

To preserve order:

```python
a = [10, 20, 10, 30, 20]

b = list(dict.fromkeys(a))

print(b)
```

Output:

```text
[10, 20, 30]
```

---

# Q134. What is a nested list?

A list containing another list is called a **nested list**.

```python
matrix = [
    [1, 2],
    [3, 4]
]
```

You can access:

```python
print(matrix[0][1])
```

Output:

```text
2
```

---

# Q135. How do you traverse a nested list?

Use nested loops.

```python
matrix = [
    [1, 2],
    [3, 4]
]

for row in matrix:
    for value in row:
        print(value)
```

Output:

```text
1
2
3
4
```

---

# Q136. What is shallow copy?

A **shallow copy** creates a new outer object but does not recursively copy nested objects.

```python
import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)
```

The outer lists are different, but nested lists are shared.

Conceptually:

```text
a ──→ outer list
       ↓
      inner list ←── b
```

Therefore, modifying a nested list can affect both.

---

# Q137. What is deep copy?

A **deep copy** recursively copies nested objects too.

```python
import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)
```

Now the nested lists are also independent.

```text
a → outer → inner
b → outer → inner
```

They don't share those nested list objects.

---

# Q138. Difference between shallow and deep copy?

| Shallow Copy                 | Deep Copy                       |
| ---------------------------- | ------------------------------- |
| Copies outer object          | Copies outer and nested objects |
| Nested objects can be shared | Nested objects are independent  |
| `copy.copy()`                | `copy.deepcopy()`               |

Example:

```python
b = copy.copy(a)
```

vs.

```python
b = copy.deepcopy(a)
```

---

# Q139. What happens in `a = b`?

No copy is created.

Both variables refer to the **same object**.

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
```

Output:

```text
[1, 2, 3, 4]
```

Conceptually:

```text
a ──┐
    ├──→ [1, 2, 3]
b ──┘
```

---

# Q140. What happens in `a = b.copy()`?

A new outer list is created.

```python
b = [1, 2, 3]

a = b.copy()

a.append(4)

print(a)
print(b)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3]
```

For nested lists, remember that `.copy()` is only a **shallow copy**.

---

# 🔵 PART 2 — PYTHON STRING QUESTIONS

## Q28. Why are strings immutable?

A string is **immutable**, meaning its contents cannot be changed after creation.

```python
s = "hello"

s[0] = "H"
```

This produces:

```text
TypeError
```

Instead, Python creates a new string:

```python
s = "hello"
s = "H" + s[1:]

print(s)
```

Output:

```text
Hello
```

The original `"hello"` wasn't modified.

### Why?

Immutability provides benefits such as:

- Safe sharing
- Hashability
- Reliable dictionary/set keys
- String interning
- Predictable behavior

---

# Q42. Why does `input()` always return a string?

`input()` receives keyboard input as **text**.

```python
age = input("Enter age: ")

print(type(age))
```

If you enter:

```text
20
```

Output:

```text
<class 'str'>
```

Even though you typed `20`, Python receives `"20"`.

To convert:

```python
age = int(input("Enter age: "))
```

---

# Q50. Can every string be converted to `int`?

No.

A string must represent a valid integer.

### Valid:

```python
int("100")
int("-50")
int("0")
```

### Invalid:

```python
int("hello")
```

Produces:

```text
ValueError
```

Also:

```python
int("10.5")
```

is invalid because `"10.5"` is not an integer representation.

You can do:

```python
int(float("10.5"))
```

which produces:

```text
10
```

---

# Q55. What is `str()`?

`str()` converts an object/value into a string representation.

```python
age = 20

x = str(age)

print(x)
print(type(x))
```

Output:

```text
20
<class 'str'>
```

This is useful when concatenating:

```python
age = 20

print("Age: " + str(age))
```

---

# Q57. What is string formatting?

String formatting means **inserting values into a string in a controlled format**.

For example:

```python
name = "Aayush"
age = 20

print(f"My name is {name} and my age is {age}")
```

Output:

```text
My name is Aayush and my age is 20
```

Common techniques include:

```text
% formatting
str.format()
f-strings
```

---

# Q58. What are f-strings?

An **f-string** is a formatted string literal that allows variables and expressions inside `{}`.

```python
name = "Aayush"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Aayush and I am 20 years old.
```

Expressions can also be used:

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output:

```text
Sum = 30
```

---

# Q59. Difference between `format()` and f-strings?

### `format()`

```python
name = "Aayush"
age = 20

print("My name is {} and I am {} years old".format(name, age))
```

### f-string

```python
print(f"My name is {name} and I am {age} years old")
```

Both perform string formatting.

| `format()`                 | f-string                       |
| -------------------------- | ------------------------------ |
| Uses `.format()`           | Uses `f""`                     |
| Values supplied separately | Variables directly inside `{}` |
| Older approach             | Modern approach                |
| Can be more verbose        | Usually more readable          |

---

# Q60. How do you print variables inside strings?

### Using f-string

```python
name = "Aayush"
age = 20

print(f"My name is {name} and age is {age}")
```

### Using `format()`

```python
print("My name is {} and age is {}".format(name, age))
```

### Using concatenation

```python
print("My name is " + name + " and age is " + str(age))
```

For modern Python, f-strings are usually the cleanest choice.

---

# Q75. What are membership operators?

Membership operators check whether a value exists in a sequence or collection.

Python has:

```python
in
not in
```

Example:

```python
name = "Aayush"

print("A" in name)
```

Output:

```text
True
```

Another:

```python
print("z" not in name)
```

Output:

```text
True
```

---

# Q76. Difference between `in` and `not in`?

### `in`

Checks whether something exists.

```python
print("a" in "Aayush")
```

Output:

```text
True
```

Python string membership is case-sensitive:

```python
print("A" in "Aayush")
```

Output:

```text
True
```

but:

```python
print("a" in "Aayush")
```

also happens to be `True` because `"Aayush"` contains lowercase `a` at position 1.

For `"PYTHON"`:

```python
print("p" in "PYTHON")
```

Output:

```text
False
```

### `not in`

Checks absence:

```python
print("z" not in "Python")
```

Output:

```text
True
```

---

# Q78. Difference between `is` and `==`?

### `==` → compares values

```python
a = [1, 2]
b = [1, 2]

print(a == b)
```

Output:

```text
True
```

The contents are equal.

### `is` → compares identity

```python
print(a is b)
```

Output:

```text
False
```

They are different list objects.

### Remember:

```text
==  → Are the values equal?
is  → Are they the same object?
```

For example:

```python
x = None

if x is None:
    print("No value")
```

`is` is commonly used with singleton objects such as `None`.

---

# Q86. What values are considered False in Python?

Python has several **falsy values**.

Common ones are:

```python
False
None
0
0.0
0j
""
[]
()
{}
set()
```

Example:

```python
print(bool(""))
print(bool([]))
print(bool(0))
print(bool(None))
```

Output:

```text
False
False
False
False
```

Most other values are truthy.

---

# Q87. What is truthiness?

**Truthiness** is Python's way of determining whether a value behaves like `True` or `False` in a Boolean context.

Example:

```python
name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")
```

Output:

```text
Name is empty
```

Because:

```python
bool("")
```

is `False`.

But:

```python
name = "Aayush"

if name:
    print("Name exists")
```

Output:

```text
Name exists
```

because a non-empty string is truthy.

---

# Q115. How do you iterate through a string?

A string is iterable, so we can use a `for` loop.

```python
name = "Aayush"

for char in name:
    print(char)
```

Output:

```text
A
a
y
u
s
h
```

You can also use indexes:

```python
for i in range(len(name)):
    print(name[i])
```

But the first approach is usually simpler.

---

# Q158. What is the output of `print(bool(''))`?

```python
print(bool(''))
```

Output:

```text
False
```

Why?

Because `''` is an **empty string**, and empty strings are falsy.

```python
bool("")
# False
```

---

# Q159. What is the output of `print(bool('0'))`?

```python
print(bool('0'))
```

Output:

```text
True
```

This is an important interview question.

`'0'` is a **non-empty string**.

Therefore:

```python
bool("0")
```

is:

```text
True
```

Compare:

```python
bool("")
# False

bool("0")
# True
```

Even:

```python
bool(" ")
```

is `True`, because it contains a space.

---

# Q172. Why does `input()` return string?

This is the same concept as Q42.

```python
name = input("Enter name: ")
```

The input received from the user is text, so Python returns it as a `str`.

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

If numeric input is required:

```python
age = int(input("Enter age: "))
```

---

# ⭐ Important String Topics Missing From Your 180 Questions

Your 180-question list has only the basic String questions. For **complete String interview preparation**, you should also study these:

| Topic               | Example                |
| ------------------- | ---------------------- |
| String creation     | `"Hello"`              |
| Indexing            | `s[0]`                 |
| Negative indexing   | `s[-1]`                |
| Slicing             | `s[1:4]`               |
| Step slicing        | `s[::2]`               |
| Concatenation       | `"Hi" + "Hello"`       |
| Repetition          | `"Hi" * 3`             |
| `len()`             | `len(s)`               |
| `upper()`           | `s.upper()`            |
| `lower()`           | `s.lower()`            |
| `capitalize()`      | `s.capitalize()`       |
| `title()`           | `s.title()`            |
| `strip()`           | `s.strip()`            |
| `split()`           | `s.split()`            |
| `join()`            | `" ".join(words)`      |
| `replace()`         | `s.replace("a", "b")`  |
| `find()`            | `s.find("a")`          |
| `index()`           | `s.index("a")`         |
| `count()`           | `s.count("a")`         |
| `startswith()`      | `s.startswith("Py")`   |
| `endswith()`        | `s.endswith("on")`     |
| `isalpha()`         | `s.isalpha()`          |
| `isdigit()`         | `s.isdigit()`          |
| `isalnum()`         | `s.isalnum()`          |
| `isspace()`         | `s.isspace()`          |
| `ord()`             | `ord("A")`             |
| `chr()`             | `chr(65)`              |
| Reversal            | `s[::-1]`              |
| Palindrome          | `s == s[::-1]`         |
| Character frequency | `s.count(char)`        |
| String interning    | `sys.intern()`         |
| String memory       | Unicode string objects |
| Escape characters   | `\n`, `\t`, `\\`       |
| Raw strings         | `r"C:\new"`            |

### One important distinction

Don't mix these two concepts:

```python
a = "hello"
```

Here `a` is a **variable referring to a string object**.

```python
a = [1, 2, 3]
```

Here `a` refers to a **list object**.

The key difference is:

```text
String → immutable
List   → mutable
```

That distinction is one of the most commonly asked Python interview concepts.
