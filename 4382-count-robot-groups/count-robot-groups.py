class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n=len(position)
        
        num=0
        while num<n:
            if num+1!=n and position[num+1]-position[num]<=distance:
                position.pop(num)
                speed.pop(num)
                n-=1
            else:
                num+=1
        res=0
        speedmin=speed[n-1]
        # print(position,speed)
        for i in range(n-1,-1,-1):
            if i-1>=0:
                if speed[i-1]>speedmin:
                    res+=1
                else:
                    speedmin=speed[i-1]
        return n-res
            
                
        