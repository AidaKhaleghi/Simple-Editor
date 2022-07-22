class Stack():
    def __init__(self, n):
        self.maxSize = n
        self.array = [0] * n
        self.top = -1
        self.size = 0
    
    def Push(self, data):
        if self.size == self.maxSize:
            return
        self.top = self.top + 1
        self.array[self.top] = data
        self.size = self.size + 1
        
    
    def Pop(self):
        if self.top == -1:
            return "can't delete!"
        temp = self.array[self.top]
        self.top = self.top - 1
        self.size = self.size - 1
        return temp

    def IsEmpty(self):
        return self.size == 0
            
    def stackSize(self):
        return self.size

    #def stackIterate(self):
        #for i in self.array:
            #return i


    def printStackElements(self):
        for i in range(0,self.size):
            print(self.Pop(), end="")


#Main Programm
inputString = input()
n = len(inputString)
firstStack = Stack(n)



for i in range(0, n):
    if inputString[i] == '&':
        firstStack.Pop()
    elif inputString[i] == '#':
        firstStack.Push('\n')
    elif (inputString[i] == ' ') and (inputString[i-1] == '#'):
        pass
    else:
        firstStack.Push(inputString[i])

seccondStack = Stack(firstStack.stackSize())

while not firstStack.IsEmpty():
    seccondStack.Push(firstStack.Pop())

seccondStack.printStackElements()