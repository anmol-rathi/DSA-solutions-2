class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        best_single = float('inf')
        ans = float('inf')
        
        i = 0
        j = 0
        total = 0
        
        while i < n:
            total += arr[i]
            
            # Shrink window whenever sum is strictly greater than target
            while total > target:
                total -= arr[j]
                j += 1
            
            if total == target:
                length = i - j + 1
                
                # Check for a non-overlapping valid subarray ending BEFORE index j
                if j > 0 and dp[j - 1] != float('inf'):
                    ans = min(ans, length + dp[j - 1])
                
                # Update the shortest single valid subarray found so far
                best_single = min(best_single, length)
            
            # Record the best length seen in arr[0...i] AT EVERY INDEX i
            dp[i] = best_single
            i += 1

        return ans if ans != float('inf') else -1
# class Solution:
#     def minSumOfLengths(self, arr: List[int], target: int) -> int:
#         n=len(arr)
#         mini1=float('inf')
#         mini2=float('inf')
#         i=0
#         j=0
#         total=0
#         while i<n:
#             while i<n and total<target:
#                 total+=arr[i]
#                 i+=1
#             # print(total,i)
#             if total==target:
#                 temp1=mini1
#                 temp2=mini2
#                 if mini1==float('inf'):
#                     mini1=i-j
#                     total=0
#                     j=i
#                 elif mini2==float('inf'):
#                     mini2=i-j
#                     total=0
#                     j=i
#                 else:
#                     if max(mini1,mini2)>i-j:
#                         if mini1>mini2:
#                             mini1=i-j
#                             total=0
#                             j=i
#                         else:
#                             mini2=i-j
#                             total=0
#                             j=i
#                 if temp1==mini1 and temp2==mini2:
#                     total-=arr[j]
#                     j+=1
#             # print(mini1,mini2)
#             while total>target:
#                 total-=arr[j]
#                 j+=1
#         if mini1==float('inf') or mini2==float('inf'):
#             return -1
#         return mini1+mini2