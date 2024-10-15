# Problem Statement: You have two lists of student names.
#  One list contains the names of students who have submitted their assignments,
#  and the other list contains the names of students who attended the last class.
# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in attended and "Alice" in submitted:
    print("Alice attended and submitted")
else: 
    print("Alice Did Not Submit or Attend")
