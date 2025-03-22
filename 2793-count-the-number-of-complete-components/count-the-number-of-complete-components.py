class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(i): 
            component.add(i)
            
            for neighbour in graph[i]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)
					
        visited = set() 
        res = 0 
        for i in range(n):
            if i not in visited:
                component = set() 
                visited.add(i)
                dfs(i)
                
                if all(len(graph[node]) == len(component)-1 for node in component):
                       res += 1 
        return res

        