# Using the stack, the procedural approach
stack = []
def push (value) :
   stack.append(value)
def pop () :
   value = stack[-1]
   del value
   return value
