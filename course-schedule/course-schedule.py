class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Make an adjacency graph mapping courses to their prerequisites
        adjGraph = {}
        for course in range(numCourses):
            adjGraph[course] = []
        for prereq in prerequisites:
            adjGraph[prereq[0]].append(prereq[1])

        # Sets holding courses visited and courses completed
        visited, completed = set(), set()

        # Run DFS from each course - Returns True if the course can be finished
        def dfs(course: int) -> bool:
            # Base Case - Current course has already been completed
            if (course in completed):
                return True

            # Base Case - Current course has no prerequisites
            if (len(adjGraph[course]) == 0):
                completed.add(course)
                return True
            
            # Recursive - Check that all prerequisites can be completed 
            else:
                visited.add(course)
                for prereq in adjGraph[course]:
                    # Prerequisite already completed
                    if (prereq in completed):
                        continue
                    # Cycle - Prerequisite has been seen before, but not completed
                    elif (prereq in visited):
                        return False
                    else: 
                        canComplete = dfs(prereq)
                        if (not canComplete):
                            return False
                completed.add(course)
                return True
        
        for course in range(numCourses):
            if (not dfs(course)):
                return False
                
        return True 
                    
        