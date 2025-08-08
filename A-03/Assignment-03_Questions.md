# Assignment - 03

**Total Marks:** 100
**Deadline:** 08/13/2025
**Topic:** Conditional statements, nested if-else, while loops in Python

---

## Topics: Conditional Statements (5 questions × 5 = 25)

1.  Write a Python program that takes a temperature input and prints:
    *   `Cold` (if temp < 15)
    *   `Warm` (if 15 ≤ temp < 30)
    *   `Hot` (if temp ≥ 30)

2.  Write a Python program that takes an accuracy input (0–100%).
    *   If accuracy ≥ 90 → `Excellent Model`
    *   If 70–89 → `Good Model`
    *   If 50–69 → `Average Model`
    *   Else → `Poor Model`

3.  Write a Python program that takes an integer dataset size as input and prints whether it is `Even` or `Odd`.

4.  Write a Python program that takes two loss values as input (`model_1_loss`, `model_2_loss`) and prints which model performs better (lower loss is better).

5.  Write a Python program that takes a message as input.
    *   If "offer" or "free" is present, then print `Spam Message`.
    *   Else → `Not Spam`

---

## Topics: Nested If-Else (5 questions × 5 = 25)

6.  Write a Python program that takes `age` and `number of published papers` as input.
    *   If `age` ≥ 18:
        *   If `papers` ≥ 2 → `Eligible for Talk`
        *   Else → `Eligible for Attendee only`
    *   Else → `Not Eligible`

7.  Write a Python program with the following inputs: `accuracy` and `latency` (ms).
    *   If `Accuracy` ≥ 85:
        *   If `Latency` ≤ 100ms → `Ready for Production`
        *   Else → `Needs Optimization`
    *   Else → `Not Suitable for Deployment`

8.  Write a Python program with the following inputs: `number of samples` and `percentage of missing values`.
    *   If `samples` ≥ 1000:
        *   If `missing` ≤ 10% → `Good Dataset`
        *   Else → `Needs Cleaning`
    *   Else → `Insufficient Data`

9.  Write a Python program with inputs: `data_source` (public/private) and `consent` (yes/no).
    *   If `data_source` == "public" → `Usable Data`
    *   Else (if private), perform a nested check:
        *   If `consent` == "yes" → `Usable Data`
        *   Else → `Ethical Issue`

10. Write a Python program with the input: `problem_type` (classification/regression) and `dataset_size`.
    *   If `classification`:
        *   If `dataset_size` ≤ 5000 → `Logistic Regression`
        *   Else → `Neural Network`
    *   If `regression`:
        *   If `dataset_size` ≤ 10000 → `Linear Regression`
        *   Else → `XGBoost`

---

## Topic: While Loops (5 questions × 5 = 25)

11. Write a Python program that takes an initial loss value as input. While `loss` > 0.1, subtract 0.05 in each iteration and print the new loss.
12. Write a Python program to create a chatbot that takes user input. It should keep responding "Bot: I am learning..." until the user types "exit."
13. Write a Python program that uses a while loop to count from 1 up to `dataset_size` and print the final count.
14. Write a Python program that takes `total_epochs` as input. For each epoch, print "Training epoch X" until all epochs are completed.
15. Write a Python program that takes a number as input. Use a while loop to keep dividing the number by 2 until the value is ≤ 1. Print each step.

---

## Combine Questions (5 questions × 5 = 25)

16. Write a Python program that takes a `password` as input.
    *   If length ≥ 8:
        *   If "AI" is present in the password → `Strong Password`
        *   Else → `Weak Password`
    *   Else → `Invalid Password`
17. Write a Python program with `learning_rate = 0.1`. While `learning_rate` > 0.001, divide it by 2 and print each new value.
18. Write a Python program that takes `dataset_labels` (a number representing the total count of labels) as input. Use a while loop to count how many even-numbered labels exist from 1 up to that number.
19. Write a Python program with `accuracy = 50`. While `accuracy` < 95, increase it by 5 and print "Current Accuracy: x%."
20. Write a Python program that takes `marks` (0-100) as input.
    *   If `marks` ≥ 80 → `AI Expert`
    *   Else if `marks` ≥ 60 → `AI Learner`
    *   Else → `Needs Improvement`