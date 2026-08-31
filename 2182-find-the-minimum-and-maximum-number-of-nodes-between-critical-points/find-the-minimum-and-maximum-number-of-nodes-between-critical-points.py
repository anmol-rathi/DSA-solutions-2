# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=None
        firstcri=-1
        count=1
        curr=-1
        mi=100000
        while head.next:
            if not prev:
                prev=head
                head=head.next
                count+=1
                continue
            if (head.val>prev.val and head.val>head.next.val) or (head.val<prev.val and head.val<head.next.val):
                if firstcri==-1:
                    firstcri=count
                if curr!=-1:  
                    mi=min(mi,count-curr)
                curr=count
            prev=head
            head=head.next
            count+=1
        # print(firstcri,curr,count,mi)
        if firstcri==curr:
            return [-1,-1]
        return [mi, curr-firstcri]





        