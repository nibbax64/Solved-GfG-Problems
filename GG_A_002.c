/*
Given an array of distinct integers.
The task is to count all the triplets such that sum of two elements equals the third element.

Input:
The first line of input contains an integer T denoting the number of test cases.
Then T test cases follow. Each test case consists of two lines.
First line of each test case contains an Integer N denoting size of array and
the second line contains N space separated elements.

Output:
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".

Constraints:
1 <= T <= 100
3 <= N <= 105
1 <= A[i] <= 106

Example:
Input:
2
4
1 5 3 2
3
3 2 7
Output:
2
-1

Explanation:
Testcase 1: There are 2 triplets: 1 + 2 = 3 and 3 + 2 = 5
*/
# include <stdio.h>
void bb_sort(int *arr, int n){
    int i, j, flag;
    for(i=0; i<n-1; i++){
        flag = 0;
        for(j=i; j<n-i-1; j++){
            if(arr[j] > arr[j+1]){
                flag = 1;
                arr[j] = arr[j] ^ arr[j+1];
                arr[j+1] = arr[j] ^ arr[j+1];
                arr[j] = arr[j] ^ arr[j+1];
            }
        }
        if(flag == 0)
            break;
    }
}
int func(int *arr, int n){
    int j, cnt=0;
    for(j=0; j<n-2; j++){
        if(arr[j]+arr[j+1] == arr[j+2]){
            cnt += 1;
        }
    }
    
    if(cnt == 0)
        return -1;
    else
        return cnt;
}
int main(){
    int i, t, n, arr[105];

    scanf("%d", &t);
    if(t>=1 && t<=100){
        while(t>0){
            scanf("%d", &n);
            if(n>=3 && n<=105){
                for(i=0; i<n; i++){
                    scanf("%d", &arr[i]);
                }
                bb_sort(arr, n);
                printf("OP : %d\n", func(arr, n));
            }
            t -= 1;
        }
        
    }
    return 0;
}