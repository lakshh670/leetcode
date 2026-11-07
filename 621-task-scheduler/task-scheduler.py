from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        time=0
        freq=Counter(tasks)
        max_heap=[-val for val in freq.values()]
        heapq.heapify(max_heap)
        q=deque()
        while max_heap or q:
            time+=1
            if max_heap:
                val=1+heapq.heappop(max_heap)
                if val:
                    q.append((val,time+n))
            if q and q[0][1]==time:
                heapq.heappush(max_heap,q.popleft()[0])
        return time

            

        



        