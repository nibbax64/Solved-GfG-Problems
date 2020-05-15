/*
Given a string s, recursively remove adjacent duplicate characters from the string s.
The output string should not have any adjacent duplicates.
 

Input:
The first line of input contains an integer T, denoting the no of test cases.
Then T test cases follow. Each test case contains a string str.

Output:
For each test case, print a new line containing the resulting string.

Constraints:
1<=T<=100
1<=Length of string<=50

Example:
Input:
2
geeksforgeek
acaaabbbacdddd

Output:
gksforgk
acac
*/
#include <stdio.h>

int strLen(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++);
    return i;
}

void func(char *arr, int len){
    int i=0, forw = i+1, flag=0;
    while(i < len){
        if(arr[i] != arr[forw]){
            if(flag == 0){
                printf("%c", arr[i]);
                i += 1;
                forw = i+1;
            }
            else{
                i = forw;
                forw = i+1;
                flag = 0;
            }
        }
        else{
            forw += 1;
            flag = 1;
        }
    }
}

int main(){
    int t;
    char arr[30];
    scanf("%d", &t);
    while(t>0){
        scanf("%s", arr);
        func(arr, strLen(arr));
		printf("\n");
        t -= 1;
    }
    return 0;
}