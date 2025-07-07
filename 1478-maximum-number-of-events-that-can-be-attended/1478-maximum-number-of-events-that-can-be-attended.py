import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        # Step 1: Sort events by start day
        events.sort()
        
        # Step 2: Min-heap to track events by their end day
        min_heap = []  
        i = 0
        n = len(events)
        count = 0

        # Step 3: Determine the last day we need to simulate
        last_day = max(end for _, end in events)

        # Step 4: Simulate each day
        for day in range(1, last_day + 1):
            # Step 4.1: Add all events starting today to heap
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Step 4.2: Remove events that already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            # Step 4.3: Attend the event that ends earliest
            if min_heap:
                heapq.heappop(min_heap)
                count += 1

            # Step 5: Break early if no events remain
            if i == n and not min_heap:
                break

        # Step 6: Return the number of events attended
        return count