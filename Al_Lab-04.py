##################### TASK 1 #####################
# Question 1 — Implement Stack using Python
# A Stack follows the LIFO (Last In, First Out) principle.
# The element inserted last is removed first.
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            return self.stack.pop()
    def display(self):
        print("Stack:", self.stack)
# Creating a stack
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("After pushing elements:")
s.display()
print("Popped element:", s.pop())
print("After popping:")
s.display()


#####################TASK 2#########################
#  Question 2 . Implement Queue using Python #
# A *Queue* follows the *FIFO (First In, First Out)* principle. 
# The element inserted first is removed first.

# class Queue:
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, item):
#         self.queue.append(item)
#     def dequeue(self):
#         if len(self.queue) == 0:
#             print("Queue is empty")
#         else:
#             return self.queue.pop(0)
#     def display(self):
#         print("Queue:", self.queue)
# # Creating a queue
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# print("After adding elements:")
# q.display()
# print("Removed element:", q.dequeue())
# print("After removing:")
# q.display()

#####################TASK 3#########################
#  Question 3 — Implement Binary Search using Python
#Binary Search is used to find the position of a target value in a *sorted array/list. 
#It repeatedly divides the search range into two halves. The algorithm works in **logarithmic time*.

# arr = [10, 20, 30, 40, 50, 60, 70]
# target = int(input("Enter number to search: "))
# low = 0
# high = len(arr) - 1
# found = False
# while low <= high:
#     mid = (low + high) // 2
#     if arr[mid] == target:
#         print("Element found at index:", mid)
#         found = True
#         break
#     elif target > arr[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1
# if found == False:
#     print("Element not found")