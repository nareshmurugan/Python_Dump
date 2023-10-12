numberOfElements=int(input())
elements=set(input().split())
noOfOperations=int(input())
operations=['intersection_update','update','symmetric_difference_update',
        'difference_update']
arrayOfOperationAndNoElements=[]
arrayOfElementToTheOperation=[]
for i in range(noOfOperations):
    operationAndNoOfElements=input().split()
    elementsToOperation=set(int(input().split()))
    arrayOfOperationAndNoElements.append(operationAndNoOfElements)

    #if operations[0]==operationAndNoOfElements[0]
     #   elements=elements.intersection_update()
