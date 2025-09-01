class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapify(heap)

        for _ in range(extraStudents):
            r, p, t = heappop(heap)
            p += 1
            t += 1
            heappush(heap, (-gain(p, t), p, t))

        total = sum(p / t for _, p, t in heap)
        return total / len(classes)