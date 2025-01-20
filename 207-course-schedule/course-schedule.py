class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_to_nxt = collections.defaultdict(list)
        nxt_to_pre = collections.defaultdict(list)
        free_courses = set(range(numCourses))
        for pre, nxt in prerequisites:
            pre_to_nxt[pre].append(nxt)
            nxt_to_pre[nxt].append(pre)
            if nxt in free_courses:
                free_courses.remove(nxt)
        
        while free_courses:
  
            course = free_courses.pop()
            numCourses -= 1
            for nxt in pre_to_nxt[course]:
               
                nxt_to_pre[nxt].remove(course)
    
                if len(nxt_to_pre[nxt]) == 0:
                    free_courses.add(nxt)

        return numCourses == 0