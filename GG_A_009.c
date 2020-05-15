/*
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

Input:
The first line contains an integer 'T' denoting the total number of test cases.
Then T testcases follow. Each testcases contains two lines of input.
The first line denotes the size of the array N.
The second lines contains the elements of the array A separated by spaces.

Output: 
For each testcase, print the sorted array.

Constraints:
1 <= T <= 500
1 <= N <= 106
0 <= Ai <= 2

Example:
Input :
2
5
0 2 1 2 0
3
0 1 0

Output:
0 0 1 2 2
0 0 1

Explanation:
Testcase 1: After segragating the 0s, 1s and 2s, we have 0 0 1 2 2 which shown in the output.
*/

# include <stdio.h>

void insertion_sort(int *arr, int len){
    int i, key, j;
    for (i=1; i<len; i++){
        key = arr[i];
        j = i-1;
        while (j>=0 && arr[j]>key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

int main(){
    int t, n, arr[25], i;

    scanf("%d", &t);
    if(t>=1 && t<=100){
        while(t>0){
            scanf("%d", &n);
            if(n>=1 && n<=107){
                for(i=0; i<n; i++)
                    scanf("%d", &arr[i]);
                insertion_sort(arr, n);
                printf("OP : ");
                for(i=0; i<n; i++)
                    printf("%d ", arr[i]);
                printf("\n");
            }
            t -= 1;
        }
    }
    return 0;
}