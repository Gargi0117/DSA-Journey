class Solution:
    def pattern12(self, N):
        spaces = 2 * (N - 1)
        # Outer loop for the number of rows
        for i in range(1, N + 1):
            # Inner loop
            for j in range(1, i + 1):
                print(j, end="")
            
            #spaces in the middle
            for j in range(1, spaces + 1):
                print(" ", end="")
            
            #numbers in decreasing order
            for j in range(i, 0, -1):
                print(j, end="")
            print()
            spaces -= 2

sol = Solution()
N = 5
sol.pattern12(N)  # Call the function 
