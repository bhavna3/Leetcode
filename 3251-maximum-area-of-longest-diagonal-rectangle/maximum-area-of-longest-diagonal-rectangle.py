class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area=0
        diag=0

        for l, w in dimensions:
            curr_diag = l * l + w * w
            if curr_diag > diag or (curr_diag == diag and l * w > area):
                diag = curr_diag
                area = l * w

        return area