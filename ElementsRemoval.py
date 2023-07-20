'''
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.
Find the minimum cost to remove all elements from the array.

Input 1:
A = [2, 1]

Input 2:
A = [5]

Output 1:
4

Output 2:
5
'''
array = list(map(int, input().split()))
array.sort(reverse = True)
cost = 0
for i in range(0,len(array)):
    cost += array[i] * (i+1)
print(cost)
