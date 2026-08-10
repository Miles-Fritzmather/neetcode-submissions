class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set) 
        for course, requirement in prerequisites: graph[course].add(requirement) 
        
        path = set()
        def hasCycle(course: int) -> bool:
            if course in path: return True  
            if course not in graph: return False    
            path.add(course)
            for c in graph[course]:
                if hasCycle(c): return True
            path.remove(course)
            graph[course] = []
            return False                                    
             
        for key in graph.keys():                                     
            if hasCycle(key): return False

        return True