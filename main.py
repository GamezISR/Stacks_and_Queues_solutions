first_Stack = [1,2,3,4]
second_Stack = [5,2,1,5,7]
third_Stack = []

def push(element, stackName):

    # do stuff here
    stackName.append(element)

    return stackName

def pop(stackName):

    # do stuff here
    last = stackName.pop()
    return last

def isEmpty(stackName):

    # this function should return as boolean True or False
    if len(stackName) == 0:
      return True
    else:
      return False


print("First stack: " + str(first_Stack))
print("Second stack: " + str(second_Stack))
print("Third stack: " + str(third_Stack))
# push a 3 onto first stack than print stack
push(3, first_Stack)
print("Pushed First stack: " + str(first_Stack))

# push a 7 and 2 into the third stack and print
push(7, third_Stack)
push(2, third_Stack)
print("Pushed third stack: " + str(third_Stack))

# pop all elements in second stack in push them into the third stack than print
while isEmpty(second_Stack) == False:
  push(pop(second_Stack),third_Stack)
print("Popped second stack: " + str(second_Stack))
print("Pushed third stack: " + str(third_Stack))

# check all stacks with isEmpty
print(isEmpty(first_Stack))
print(isEmpty(second_Stack))
print(isEmpty(third_Stack))







first_Queue = [1,2,3,4]
second_Queue = [5,2,1,5,7]
third_Queue = []

def enqueue(element, queueName):

    # do stuff here
    queueName.append(element)
    return queueName

def dequeue(queueName):

    # do stuff here
    first = queueName.pop(0)
    return first

def isEmpty(queueName):

    # this function should return as boolean True or False

    if len(queueName) == 0:
      return True
    else:
      return False


# enqueue a 3 onto first queue than print 
# enqueue a 7 and 2 into the third queue and print
# dequeue all elements in second queue and enqueue into the third queue than print
# print all queues with isEmpty












