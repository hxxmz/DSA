from typing import List
# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        yl = 0
        yr = m - 1

        while yl <= yr:
            ym = (yl + yr) // 2

            xl = 0
            xr = n - 1

            if target < matrix[ym][xl]:
                yr = ym - 1
            elif target > matrix[ym][xr]:
                yl = ym + 1
            else:
                while xl <= xr:
                    xm = (xl + xr) // 2
                    if matrix[ym][xm] == target:
                        return True
                    elif matrix[ym][xm] < target:
                        xl = xm + 1
                    else:
                        xr = xm - 1
                return False

# Test Function
def test():
    sol = Solution()
    
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),  # Exists in the matrix
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False), # Does not exist
        # ([[1, 2, 3, 4, 5]], 3, True),                                    # Single row, target present
        # ([[1], [2], [3], [4], [5]], 4, True),                            # Single column, target present
        # ([[1], [2], [3], [4], [5]], 6, False),                           # Single column, target absent
        # ([[]], 1, False),                                                # Empty matrix
        # ([[1]], 1, True),                                                # Single element, target present
        # ([[2]], 1, False),                                               # Single element, target absent
        # ([[1, 3]], 3, True),                                             # Two elements, target present
        # ([[1, 3]], 2, False),                                            # Two elements, target absent
    ]

    for i, (matrix, target, expected) in enumerate(test_cases):
        result = sol.searchMatrix(matrix, target)
        print(f"Test case {i + 1}: {'✅' if result == expected else '❌'} | Output: {result} | Expected: {expected}")

if __name__ == "__main__":
    test()