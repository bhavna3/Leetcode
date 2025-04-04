class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        # Step 1: Create a graph
        indegree = defaultdict(int)  # Count of missing ingredients
        graph = defaultdict(list)  # Dependency graph
        
        for recipe, ing_list in zip(recipes, ingredients):
            indegree[recipe] = len(ing_list)  # Count of required ingredients
            for ing in ing_list:
                graph[ing].append(recipe)  # ing -> recipes dependent on it
        
        # Step 2: Initialize queue with available supplies
        queue = deque(supplies)
        result = []
        available = set(supplies)  # Fast lookup for available items
        
        # Step 3: Process queue (Topological Sorting)
        while queue:
            item = queue.popleft()
            if item in indegree:  # Only recipes are tracked in indegree
                result.append(item)
            
            for recipe in graph[item]:
                indegree[recipe] -= 1  # Reduce missing ingredient count
                if indegree[recipe] == 0:  # If all ingredients available
                    queue.append(recipe)
                    available.add(recipe)
        
        return result
        