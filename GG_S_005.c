/*
Given two strings a and b.
The task is to find if a string 'a' can be obtained by rotating another string 'b' by 2 places.

Input:
The first line of input contains an integer T denoting the no of test cases.
Then T test cases follow. In the next two line are two string a and b.

Output:
For each test case in a new line print 1
if the string 'a' can be obtained by rotating string 'b' by two places else print 0.

Constraints:
1 <= T <= 50
1 <= length of a, b < 100

Example:
Input:
2
amazon
azonam
geeksforgeeks
geeksgeeksfor

Output:
1
0

Explanation:
Testcase 1: amazon can be rotated anti-clockwise by two places, which will make it as azonam.

Testcase 2: geeksgeeksfor can't be formed by any rotation from the given word geeksforgeeks.
*/

#include <stdio.h>

int strLen(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++);
    return i;
}
 
int func(char *str1, int len1, char *str2, int len2){
    int i, flag=1;

    if(len1 != len2)
        return 0;

    for(i=0; i<len1-2; i++){
        if(str1[i+2] != str2[i]){
            flag = 0;
            break;
        }
    }
    if(flag==1 && str1[0]==str2[len1-2] && str1[1]==str2[len1-1])
        return 1;

    flag = 1;
    for(i=0; i<len1-2; i++){
        if(str1[i] != str2[i+2]){
            flag = 0;
            break;
        }
    }
    if(flag==1 && str1[len1-1]==str2[1] && str1[len1-2]==str2[0])
        return 1;
    
    return 0;
}

int main(){
    int t;
    char arr_1[24], arr_2[24];

    scanf("%d", &t);
    while(t>0){
        scanf("%s", &arr_1);
        scanf("%s", &arr_2);
        printf("OP : %d\n", func(arr_1, strLen(arr_1), arr_2, strLen(arr_2)));
        t -= 1;
    }
    return 0;
}