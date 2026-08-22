class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            # Directed edge from prereq -> course
            graph[prereq].append(course)
            in_degree[course] += 1

        # Queue all courses that have 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        # Process courses iteratively using BFS
        while queue:
            curr = queue.popleft()
            order.append(curr)

            # Reduce the remaining prerequisite count for dependent courses
            for neighbor in graph[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If order contains all courses, we found a valid schedule.
        # Otherwise, a cycle exists and it's impossible to finish all courses.
        return order if len(order) == numCourses else []