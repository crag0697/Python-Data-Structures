# Stacks

## Overview

List or arrays are a feature of all programming languages. Their usefulness allows us to apply them in a number of unique ways. The Stack is an application of Python lists characterized by the order that elements are added or removed.

## Key Terms

- Stack: A data structure which is dependent on the order in which elements are added or removed with the Last In, First Out rule.
- LIFO: Last In, First Out. Items entered last in the list are the first to be removed.
- Front: The first index of the stack, most often index 0.
- Back: Then end of a Stack where push and pop operations are performed.
- Push: An operation that adds a new item onto the back of the stack
- Pop: An operation that removes an existing item from the back of a stack

## Stacks in the Real World

It is almost certain that you have interacted with stacks in the real world during day-to-day activities. 

### Dishes

Consider when you would put away dishes in the cupboards. Each time you stack a plate or bowl in the cupboard, you are performing what we would term a **PUSH** operation. Once the dishes are all put away, we can realize that the dishes must be removed from the top first in order to get to the first one you put down. Of course, for this example the bottom of the stack would be the front and the top would be the back of the stack. When you go to set out the dishes again, you are executing a **POP** operation by removing the plates one by one from the top of the stack. Removing from the middle of the stack would be more difficult in this example and we wouldn't 
pull from the middle of a python stack either. All operations are performed from the back of the stack.

![Stacking Plates LIFO](plate_stack.jpeg)

### Undo Function

A more direct example of a stack in everyday use is the Undo function in word processors or text editors. Consider a sentence being typed as a stack where each word is added to a stack. We would read the sentence from the screen as "Every good boy does fine." In a python list, this may appear as:
```python
sentence = ["Every", "good", "boy", "does", "fnie"]
```

Each word is appended onto the sentence forming the stack. When we make a mistake like in this example, we simply enter the Undo command which pops the most recent word from the stack
```python
sentence = ["Every", "good", "boy", "does", "fnie"]
edit = input()
if edit == "undo":
    sentence.pop()
print(sentence)
```
leaving the new sentence as "Every good boy does". The stack maintains the history of a series of items so we can perform operations related to the sequence of events.

## Methods

We've already explored push and pop operations a little so far. All operations that modify the stack do so starting from the end of the stack only. For this we use .append(x) to add and .pop() to remove items. There are additional methods that we can use to analyze the state of a stack. Notice that the efficiency of these operations is always O(1).

| Operation/Method     | Use               | Python Syntax        | Big O Efficiency      |
| -------------------- | ----------------- | -------------------- | --------------------- |
| push(value)          |Add (value) to the | stack.append(value)  | O(1) single operation |
|                      |end of the stack   |                      | adding to the array   |
| pop                  |Removes and returns| value = stack.pop()  | O(1) single operation |
|                      |the last element   |                      |removing from the array|
| size()               |Returns the size of| length = len(stack)  | O(1) single operation |
|                      |the stack          |                      | returning the size    |
| empty()              |Returns true if the| if len(stack) == 0   | O(1) single operation |
|                      |length is 0        |                      | adding to the array   |

## The Function Stack

To this point, we have actually been utilizing stacks in every program we have written anytime we call a function. The function call essentially tells the computer we want to: call x function, and where to return to when done. Calling the function is easy to visualize when we initiate a function call. But what about when the function needs to call a series of other functions to finish? This is done by creating what's called a call stack. 
