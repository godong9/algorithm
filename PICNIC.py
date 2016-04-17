import sys

def sanitizeAreFriends(tempMArray):
    areFriends = []
    for tempM in tempMArray:
        if tempM[0] < tempM[1]:
            areFriends.append((tempM[0], tempM[1]))
        else:
            areFriends.append((tempM[1], tempM[0]))
    return areFriends

def makeInitTakenArray(n):
    takenArray = []
    for i in xrange(0, n):
        takenArray.append(False)
    return takenArray

def countPairings(taken, n):
    firstFree = -1
    for i in xrange(0, n):
        if not taken[i]:
            firstFree = i
            break
    if firstFree == -1:
        return 1
    ret = 0
    pairWith = firstFree + 1
    while pairWith < n:
        if not taken[pairWith] and (firstFree, pairWith) in areFriends:
            taken[firstFree] = taken[pairWith] = True
            ret += countPairings(taken, n)
            taken[firstFree] = taken[pairWith] = False
        pairWith += 1
    return ret

testCaseN = int(raw_input().strip())
nArray = []
mArray = []

for testN in xrange(0, testCaseN):
    arr = map(int, raw_input().strip().split(' '))
    nArray.append(arr[0])
    mSize = int(arr[1])
    mArr = []
    if mSize > 0:
        mArr = map(int, raw_input().strip().split(' '))
    mIdx = 0
    tempMArray = []
    for mArrayN in xrange(0, mSize):
        tempMArray.append([mArr[mIdx], mArr[mIdx + 1]])
        mIdx += 2
    mArray.append(tempMArray)

#print nArray
#print mArray

for i in xrange(0, len(nArray)):
    n = nArray[i]
    areFriends = sanitizeAreFriends(mArray[i])
    print countPairings(makeInitTakenArray(n), n)

