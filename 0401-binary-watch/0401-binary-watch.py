class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # Initialize the output list to store valid times
        output = []

        # Loop through all possible hours (0 to 11)
        for h in range(12):
            # Loop through all possible minutes (0 to 59)
            for m in range(60):
                # Count the number of '1's in the binary representation of the hour and minute
                # If their sum equals the number of LEDs that are turned on, it's a valid time
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Format the time as "h:mm" with zero-padded minutes (e.g., "3:07")
                    output.append(f"{h}:{m:02d}")

        # Return the list of all valid times
        return output