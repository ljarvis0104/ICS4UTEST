def getBASIC():
    list = []
    n = input()
    while True:
        line = n
        if n.endswith('END'):
            list.append(line)
            return list
        else:
            list.append(line)
            newN = input()
            n = newN
def findLine(prog, target):
     for i in range(0,len(prog)):
         if prog[i].startswith(target):
            return i
def execute(prog):
    location = 0
    while True:
        if location == len(prog) - 1:
            return 'success'
        theList = prog[location].split()
        T = theList[2]
        previous = theList[0]
        location = findLine(prog, T)
        theList = prog[location].split()
        if len(theList) == 3:
            present = theList[2]
            if previous == present:
                return 'infinite loop'
print(execute(getBASIC()))