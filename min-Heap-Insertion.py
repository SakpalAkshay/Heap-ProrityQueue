class MinHeap:
    def __init__(self):
        self.arr = []
    
    #here are the main heap functions
    def insert(self,x):
        #we will first append new element in the end but that will cause violation of heap properties
        #time complexity should be logN

        #min heap approach => we will added to the end and then we will check if parent is bigger
        # if Parent is bigger we will swap, we will keep swapping unitl we reach end (root) or we find a parent thats smaller
        # Min Heap property is Each Descendent when compared to Root is bigger that root, this also applies in each and every subtree
        self.arr.append(x)
        i = len(self.arr) - 1 #because we appended at end, the end would be our current index 
        # we will keep swapping until our i is at proper index or i becomes 0 or root
        while i > 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p #index gets updated to parents so we compare with the new parent after Swapping
    #utility function
    def parent(self,i):
        #return the index of parent provided ith element
        return (i -1) // 2 #using the formula
