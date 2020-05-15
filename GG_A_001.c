/*
Given an unsorted array A of size N of non-negative integers,
find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case consists of two lines.
The first line of each test case is N and S, where N is the size of array and S is the sum.
The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line,
print the starting and ending positions(1 indexing) of first such occuring subarray from the left
if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
*/
# include <stdio.h>
void func(int *arr, int n, int m){
    int i, j, sum, pos[2]={0};

    for(i=0; i<n; i++){
        sum = 0;
        for(j=i; j<n; j++){
            if(sum+arr[j] <= m)
                sum += arr[j];
            else
                break;
        }
        if(sum == m){
            pos[0] = i+1;
            pos[1] = j;
            break;
        }
    }
    if(pos[0] == 0 && pos[1] == 0)
        printf("OP : -1\n");
    else
        printf("OP : %d %d\n",pos[0],pos[1]);
    
}
int main(){
    int t, n, m, arr[107], i;

    scanf("%d", &t);
    if(t>=1 && t<=100){
        while(t>0){
            scanf("%d%d", &n, &m);
            if(n>=1 && n<=107){
                for(i=0; i<n; i++){
                    scanf("%d", &arr[i]);
                }
                func(arr, n, m);
            }
            t -= 1;
        }
    }
    return 0;
}