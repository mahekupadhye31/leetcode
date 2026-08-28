from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices, values kept in decreasing order
        result = []

        for right in range(len(nums)):
            # 1. Back-pop: remove indices whose values are smaller than the new one
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # 2. Push the new index
            dq.append(right)

            # 3. Front-expiry: remove the front index if it's fallen outside the window
            if dq[0] <= right - k:
                dq.popleft()

            # 4. Record the max once we have a full window
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result