/*
Given a string S. The task is to print all permutations of a given string.

Input:
The first line of input contains an integer T, denoting the number of test cases.
Each test case contains a single string S in capital letter.

Output:
For each test case, print all permutations of a given string S with single space and
all permutations should be in lexicographically increasing order.

Constraints:
1 ≤ T ≤ 10
1 ≤ size of string ≤ 5

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA

Explanation:
Testcase 1: Given string ABC has permutations in 6 forms as ABC, ACB, BAC, BCA, CAB and CBA .
*/
#include <stdio.h>

int strLen(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++);
    return i;
}

void swap(char *a, char *b){
    char temp = *a;
    *a = *b;
    *b = temp;
}

void func(char *arr, int left, int right){

    int i;

    if(left == right)
        printf("%s ", arr);
    else
        for(i=left; i<=right; i++){
            swap((arr+left),(arr+i));
            func(arr, left+1, right);
            swap((arr+left),(arr+i));
        }
}

int main(){
    int t;
    char arr[10];

    scanf("%d", &t);
    while(t>0){
        scanf("%s", arr);
        printf("OP : ");
        func(arr, 0, strLen(arr)-1);
		printf("\n");
        t -= 1;
    }
    return 0;
}
/*
ABC 0 2
    i=0
    ABC->ABC
    ABC 1 2
        i=1
        ABC->ABC
        ABC 2 2
            OP-ABC
        ABC->ABC
        i=2
        ABC->ACB
        ACB 2 2
            OP-ACB
        ACB->ABC
        i=3
    ABC->ABC
    i=1
    ABC->BAC
    BAC 1 2
        i=1
        BAC->BAC
        BAC 2 2
            OP-BAC
        BAC->BAC
        i=2
        BAC->BCA
        BCA 2 2
            OP-BCA
        BCA->BAC
        i=3
    BAC->ABC
    i=2
    ABC->CBA
    CBA 1 2
        i=1
        CBA->CBA
        CBA 2 2
            OP-CBA
        CBA->CBA
        i=2
        CBA->CAB
        CAB 2 2
            OP-CAB
        CAB->CBA
        i=3
    CBA->ABC
    i=3
*/