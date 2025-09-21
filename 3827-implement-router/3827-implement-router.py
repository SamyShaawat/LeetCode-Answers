from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.buffer = deque()  
        self.seen = set()      
        self.dest_to_timestamps = defaultdict(list)  

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet_id = (source, destination, timestamp)
        
        if packet_id in self.seen:
            return False
        
        if len(self.buffer) >= self.limit:
            old_src, old_dst, old_time = self.buffer.popleft()
            self.seen.remove((old_src, old_dst, old_time))
            
            ts_list = self.dest_to_timestamps[old_dst]
            idx = bisect.bisect_left(ts_list, old_time)
            if idx < len(ts_list) and ts_list[idx] == old_time:
                ts_list.pop(idx)

        self.buffer.append((source, destination, timestamp))
        self.seen.add(packet_id)
        bisect.insort(self.dest_to_timestamps[destination], timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.buffer:
            return []

        src, dst, time = self.buffer.popleft()
        self.seen.remove((src, dst, time))
        
        ts_list = self.dest_to_timestamps[dst]
        idx = bisect.bisect_left(ts_list, time)
        if idx < len(ts_list) and ts_list[idx] == time:
            ts_list.pop(idx)

        return [src, dst, time]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts_list = self.dest_to_timestamps[destination]
        left = bisect.bisect_left(ts_list, startTime)
        right = bisect.bisect_right(ts_list, endTime)
        return right - left
