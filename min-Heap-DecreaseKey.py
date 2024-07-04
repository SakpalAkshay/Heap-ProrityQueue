def parent(i):
  return (i - 1) //2 # return parent index of Ith Node


def decreaseKey(heap,i,x): # here I is the index and x is value to replace value at I, 
  #decrease work on the premise of Insertion in Heap here we replace given value with value provided and then Heap Up to 
  #satisfy the Min heap properties
  heap[i] = x

  while i > 0 and heap[parent(i)] > heap[i]:
    p = parent(i)
    heap[i],heap[p] = heap[p],heap[i]
    i = p
  
   
  
