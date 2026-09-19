class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestx=max(x1,min(xCenter,x2))
        closesty=max(y1,min(yCenter,y2))
        dx=xCenter-closestx
        dy=yCenter-closesty
        return dx*dx + dy*dy <=radius*radius
