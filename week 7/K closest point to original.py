class Solution(object):
    def kClosest(self, points, k):
        def distance(x,y):
            return pow(x,2)+pow(y,2)
        points.sort(key = lambda x: distance(x[0],x[1]))
        return points[:k] 
