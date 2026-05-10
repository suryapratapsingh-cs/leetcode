import heapq

class Solution:
    def minCost(self, n: int, prices: list[int], roads: list[list[int]]) -> list[int]:
        # adj1 for forward trip (cost)
        # adj2 for return trip (cost * tax)
        adj1 = [[] for _ in range(n)]
        adj2 = [[] for _ in range(n)]
        
        for u, v, c, t in roads:
            adj1[u].append((v, c))
            adj1[v].append((u, c))
            adj2[u].append((v, c * t))
            adj2[v].append((u, c * t))
            
        def get_dists(start_node, adj):
            dist = [float('inf')] * n
            dist[start_node] = 0
            pq = [(0, start_node)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]: 
                    continue
                for v, weight in adj[u]:
                    if d + weight < dist[v]:
                        dist[v] = d + weight
                        heapq.heappush(pq, (dist[v], v))
            return dist

        ans = []
        # For each shop i, find the minimum total cost by checking all possible destination shops j
        for i in range(n):
            dist_forward = get_dists(i, adj1)
            dist_return = get_dists(i, adj2)
            
            # Total Cost = Forward(i -> j) + Return(j -> i with tax) + Price(j)
            min_c = min(dist_forward[j] + dist_return[j] + prices[j] for j in range(n))
            ans.append(min_c)
            
        return ans
