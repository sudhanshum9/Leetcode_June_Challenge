class Solution(object):
    def findItinerary(self, tickets):

        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)
        print(self.flightMap)

        for origin, itinerary in self.flightMap.items():
        #
            itinerary.sort(reverse=True)
        print(self.flightMap)
        self.result = []
        self.DFS('JFK')


        return self.result[::-1]

    def DFS(self, origin):
        destList = self.flightMap[origin]
        while destList:
            #while we visit the edge, we trim it off from graph.
            nextDest = destList.pop()
            self.DFS(nextDest)
        self.result.append(origin)