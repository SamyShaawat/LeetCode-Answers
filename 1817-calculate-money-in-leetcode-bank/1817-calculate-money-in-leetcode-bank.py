class Solution:
    def totalMoney(self, n: int) -> int:

        # Number of complete weeks
        weeks = n // 7
        # Remaining days in the last week
        days = n % 7

        # Sum for complete weeks
        # Each week starts with +1 more than the previous one
        # Formula for sum of an arithmetic series:
        # Sum = number_of_terms / 2 * (first_term + last_term)
        # For weeks: each week total = 7 * (2 * start + 6) / 2
        total = 0
        for w in range(weeks):
            total += 7 * (2 * (1 + w) + 6) // 2

        # Sum for remaining days of the last (incomplete) week
        start = weeks + 1
        for d in range(days):
            total += start + d

        return total
