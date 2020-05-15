/*
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases.
The description of T test cases follows.
The first line of each test case contains a single integer N denoting the size of array.
The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1

Explanation:
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
*/
# include <stdio.h>
# define max(a,b) (a>b)?a:b
int func(int *arr, int n){
    int i, max_so_far=arr[0], current_max=arr[0];
    for(i=1; i<n; i++){
        current_max = max(arr[i], current_max+arr[i]);
        max_so_far = max(max_so_far, current_max);
    }
    return max_so_far;
}
int main(){
    int t, n, arr[106], i;
    scanf("%d", &t);
    if(t>=1 && t<=110){
        while(t){
            scanf("%d", &n);
            if(n>=1 && n<=106){
                for(i=0; i<n; i++)
                    scanf("%d", &arr[i]);
                printf("OP : %d\n", func(arr, n));
            }
            t -= 1;
        }
    }
    return 0;
}