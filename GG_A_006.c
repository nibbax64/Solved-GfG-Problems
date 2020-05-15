/*
Given a sorted array of positive integers.
Your task is to rearrange  the array elements alternatively i.e
first element should be max value, second should be min value, third should be second max,
fourth should be second min and so on...

Note: O(1) extra space is allowed. Also, try to modify the input array as required.

Input:
First line of input conatins number of test cases T.
First line of test case contain an integer denoting the array size N and second line of test case
contain N space separated integers denoting the array elements.

Output:
Output the modified array with alternated elements.

Constraints:
1 <=T<= 100
1 <=N<= 107
1 <=arr[i]<= 107

Example:
Input:
2
6
1 2 3 4 5 6
11 
10 20 30 40 50 60 70 80 90 100 110

Output:
6 1 5 2 4 3
110 10 100 20 90 30 80 40 70 50 60

Explanation:
Testcase 1: Max element = 6, min = 1, second max = 5, second min = 2, and so on... Modified array is : 6 1 5 2 4 3.
*/

#include <stdio.h>

void func(int *arr, int len){
    int i;
    
    for(i=0; i<len/2; i++)
        printf("%d %d ", arr[len-1-i], arr[i]);

    if(len%2 != 0)
        printf("%d", arr[len/2]);
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
                //insertion_sort(arr, n);
                printf("OP : ");
                func(arr, n);
                printf("\n");
            }
            t -= 1;
        }
    }
    return 0;
}