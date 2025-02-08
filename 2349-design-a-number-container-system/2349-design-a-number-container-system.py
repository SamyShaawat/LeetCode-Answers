class NumberContainers:

    def __init__(self):
        # Initializing the defaultdict with SortedSet and the regular dictionary
        # Map from number to set of indices
        self.number_to_indices = collections.defaultdict(SortedSet)
        # Map from index to number
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:
        # If index already has a number, remove it from the old number's index set
        if index in self.index_to_number:
            previous_number = self.index_to_number[index]
            self.number_to_indices[previous_number].remove(index)
            if not self.number_to_indices[previous_number]:
                del self.number_to_indices[previous_number]

        # Update the number and add the index to the new number's set
        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        # Return the smallest index for the given number, or -1 if not found
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)