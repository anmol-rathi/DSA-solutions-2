class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def datef(date):
            m=int(date[:2])
            d=int(date[3:])
            return sum(month[:m-1])+d
        return max(0,min(datef(leaveAlice),datef(leaveBob))-max(datef(arriveAlice),datef(arriveBob))+1)

