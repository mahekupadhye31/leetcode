class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap=[]
        queue=deque()
        count=defaultdict(int)
        total=0

        for task in tasks:
            count[task]+=1

        for key,value in count.items():
            maxheap.append(-value)

        heapq.heapify(maxheap)

        while maxheap or queue:
            # if theres a task to run, as maxheap stores the available tasks, u will run that task
            if maxheap: 
                cnt= 1+heapq.heappop(maxheap)
                if cnt:  #for A, if more occurences r still there, we put it in the queue
                    queue.append([cnt,total+n])
            if queue and total==queue[0][1]:
                cnt,time=queue.popleft()
                heapq.heappush(maxheap,cnt)
            total=total+1
        return total