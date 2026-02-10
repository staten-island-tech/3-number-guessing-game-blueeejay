---

# Python Lesson: While Loops

## 🎯 Learning Goal

Students will understand how to use **while loops** in Python to repeat code until a condition is no longer true.

---

## 1. What is a While Loop?

A **loop** is when a computer repeats something for you.

* Instead of writing the same line over and over, you tell the computer:
  *“Keep doing this until I say stop.”*

A **while loop** repeats as long as the condition (a True/False question) is **True**.

Think of it like this:
👉 “While it’s raining, I’ll stay inside.”
👉 As soon as it’s **not raining**, I’ll stop.

---

## 2. The Structure of a While Loop

```python
while condition:
    # code that repeats
```

* **`while`** is the keyword.
* **condition** is a test that must be **True** for the loop to keep going.
* The code indented under the loop will run again and again.

---

## 3. A Simple Example

```python
count = 1

while count <= 5:
    print("This is loop number", count)
    count = count + 1
```

### 🔎 What happens here?

* Start with `count = 1`.
* The computer checks: Is `count <= 5`?

  * If yes → print the message, then add 1 to `count`.
  * If no → stop the loop.
* The loop prints the message **5 times**, then stops.

---

## 4. Important: Avoid Infinite Loops 🚨

If your condition **never becomes False**, the loop never ends.
Example:

```python
number = 1
while number > 0:
    print("This will never stop!")
```

⚠️ This runs forever because `number > 0` is always True.

---

## 5. Real-Life Example (New One 🚗🍔)

Imagine you’re at a drive-thru, and you want to keep asking for items until the customer says `"done"`.

```python
order = ""

while order != "done":
    order = input("What would you like to order? (type 'done' to finish): ")

print("Thanks for your order!")
```

* The loop keeps asking until the customer types `"done"`.
* Once they type `"done"`, the loop ends.

---

## 6. Optional Challenge Problems 🧩

### Challenge 1

Write a while loop that prints the numbers from 10 down to 1.
(Hint: start at 10 and subtract 1 each time.)

### Challenge 2

Make a while loop that asks the user their favorite color until they type `"stop"`.

---

## ✅ Summary

* A **while loop** keeps repeating **as long as the condition is True**.
* Always make sure your loop will **eventually stop**.
* Use while loops for things where you don’t know how many times it should repeat (like waiting for `"done"`).

---
