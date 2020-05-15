/*
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing,
the missing number is to be found.

Input:
The first line of input contains an integer T denoting the number of test cases.
For each test case first line contains N(size of array). The subsequent line contains N-1 array elements.

Output:
Print the missing number in array.

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 107
1 ≤ C[i] ≤ 107

Example:
Input:
2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

Output:
4
9

Explanation:
Testcase 1: Given array : 1 2 3 5. Missing element is 4.
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
    int i, f;
    if(arr[1]-arr[0] == arr[2]-arr[1])
        f = arr[1]-arr[0];
    else
        f = arr[3]-arr[2];
    for(i=1; i<n-1; i++){
        if(arr[i-1]+f != arr[i]){
            return arr[i-1]+f;
        } 
    }
    return -1;
}
int main(){
    int t, n, arr[107], i;
    scanf("%d", &t);
    if(t>=1 && t<=200){
        while (t>0){
            scanf("%d", &n);
            if(n>=1 && n<=107){
                for(i=0; i<n-1; i++)
                    scanf("%d", &arr[i]);
                bb_sort(arr, n-1);
                printf("OP : %d\n", func(arr, n));
            }
            t -= 1;
        }
    }
    return 0;
}