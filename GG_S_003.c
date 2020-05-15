/*
Given a string S, find the longest palindromic substring in S.
Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S).
Palindrome string: A string which reads the same backwards.
More formally, S is palindrome if reverse(S) = S. Incase of conflict,
return the substring which occurs first ( with the least starting index ).

NOTE: Required Time Complexity O(n2).

Input:
The first line of input consists number of the testcases. The following T lines consist of a string each.

Output:
In each separate line print the longest palindrome of the string given in the respective test case.

Constraints:
1 ≤ T ≤ 100
1 ≤ Str Length ≤ 104

Example:
Input:
1
aaaabbaa

Output:
aabbaa

Explanation:
Testcase 1: The longest palindrome string present in the given string is "aabbaa". 
*/
#include <stdio.h>

int strLen(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++);
    return i;
}

void func(char *str, int len){

    int maxLength=1, i, start=0, low, high;
    
    for (i=1; i<len; i++) 
    {
        low = i-1; 
        high = i; 
        while(low>=0 && high<len && str[low]==str[high]) 
        { 
            if (high-low+1 > maxLength) 
            { 
                start = low; 
                maxLength = high-low+1; 
            } 
            low--; 
            high++; 
        }
        low = i-1; 
        high = i+1; 
        while(low>=0 && high<len && str[low]==str[high]) 
        { 
            if (high-low+1 > maxLength) 
            {
                start = low; 
                maxLength = high-low+1; 
            }
            low--;
            high++;
        }
    } 
    printf("OP : ");
    for(i=start; i<start+maxLength; i++){
        printf("%c", str[i]);
    }
    printf("\n");
}

int main(){
    int t;
    char arr[24];

    scanf("%d", &t);
    while(t>0){
        scanf("%s", &arr);
        func(arr, strLen(arr));
        t -= 1;
    }
    return 0;
}