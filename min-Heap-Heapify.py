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

    # The function doesn't return anything, it modifies the list in place

# Example usage
pq = [3, 1, 6, 5, 2, 4]  # This list represents a binary heap
heapify_down(pq, 0)      # This will heapify the element at index 0 down the heap, this is to balance the min heap after we removed the min element
print(pq)                # Output the modified heap
