from typing import List

# 54. Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        answer = [0] * (m * n)

        lb = 0
        rb = 0

        direction = 1
        horizontal = True

        # to handle bounds further maybe place an index on answer array to know how many elements scanned 
        # and cut off main loop through that, because middle indices require more than one appearances
        # think of something to handle bounds
        # you can also use directions template to escape many conditions;
        # use dirs (r,c) = ( (0,1),(1,0),(0,-1),(-1,0) ) , 0 for constant / non-zero for progression

        # to be continued
    

        print(len(answer))

# Test function
def test():
    sol = Solution()

    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),  # Expected output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),  # Expected output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        ([[1]], [1]),  # Expected output: [1]
        ([[1,2],[3,4]], [1, 2, 4, 3])  # Expected output: [1, 2, 4, 3]
    ]

    print("Testing spiralOrder:")
    for i, (matrix, expected) in enumerate(test_cases):
        result = sol.spiralOrder(matrix)
        print(f"Test case {i + 1}:")
        print(f"  Output: {result} | Expected: {expected} {'✅' if result == expected else '❌'}")

if __name__ == "__main__":
    test()
