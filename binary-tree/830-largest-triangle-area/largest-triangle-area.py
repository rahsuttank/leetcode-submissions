class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        i, j, k = 0, 0, 0
        area = 0
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i, len(points)):
                x2, y2 = points[j][0], points[j][1]
                for k in range(j, len(points)):
                    x3, y3 = points[k][0], points[k][1]
                    curArea = (1/2) * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                    area = max(area, curArea)

        return area
