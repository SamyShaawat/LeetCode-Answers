class Solution:
    def closestMeetingNode(self, edges, node1, node2):
        dist1 = self.getDistances(edges, node1)
        dist2 = self.getDistances(edges, node2)

        result = -1
        minDistance = float('inf')

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                maxDist = max(dist1[i], dist2[i])
                if maxDist < minDistance:
                    minDistance = maxDist
                    result = i
        return result

    def getDistances(self, edges, start):
        n = len(edges)
        dist = [-1] * n
        d = 0
        while start != -1 and dist[start] == -1:
            dist[start] = d
            d += 1
            start = edges[start]
        return dist