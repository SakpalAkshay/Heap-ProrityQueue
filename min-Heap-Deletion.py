# for deletion we will use 2 min heap function i.e decrease key and Heapify
#Intution is Replace the value to be deleted with -inf and then move -inf to top, through decrease min now utilize extract min to remove this -inf and heapify down
def heapify_down(pq, parent_index):
    # Initialize the indices for the parent and its children
    left_child_index = 2 * parent_index + 1
    right_child_index = 2 * parent_index + 2
    min_index = parent_index

    # Continue while the left child index is within the bounds of the heap
    while left_child_index < len(pq):
        # Check if the left child is smaller than the parent
        if pq[left_child_index] < pq[parent_index]:
            min_index = left_child_index
        
        # Check if the right child is within bounds and is the smallest
        if right_child_index < len(pq) and pq[right_child_index] < pq[min_index]:
            min_index = right_child_index

        # If the parent is already the smallest, the heap property is satisfied
        if min_index == parent_index:
            break

        # Swap the smallest child with the parent
        pq[min_index], pq[parent_index] = pq[parent_index], pq[min_index]

        # Update the parent index to the index of the smallest child
        parent_index = min_index
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

def extractMin(heap):
  if(len(heap) == 0):
    return -1;
  
  minVal = heap[0];
  size  = len(heap);
  heap[0], heap[size - 1] = heap[size - 1], heap[0]
  heap.pop()
  heapify_down(heap, 0) #this will balance the min heap
  return minVal


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
  
   
  
