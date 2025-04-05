class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Initialize the answer array with zeros, one for each box
        answer = [0] * len(boxes)

        # Loop through each box to check if it contains a ball
        for current_box in range(len(boxes)):
            # If the current box contains a ball ('1'), simulate moving it to every other box
            if boxes[current_box] == "1":
                # For each possible target box, calculate the distance (number of operations needed)
                for new_position in range(len(boxes)):
                    # Add the distance from current_box to new_position to the total operations needed for that position
                    answer[new_position] += abs(new_position - current_box)

        # Return the final list containing total operations needed to bring all balls to each box
        return answer
