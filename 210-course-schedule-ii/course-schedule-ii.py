class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        inDegree = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}

        for target, pre in prerequisites:
            graph[pre].append(target)
            inDegree[target] += 1
        
        queue = [i for i in range(numCourses) if inDegree[i] == 0]
        
        while queue:
            node = queue.pop(0)
            order.append(node)
            
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []