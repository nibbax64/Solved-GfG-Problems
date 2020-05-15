/*
Given two strings a and b consisting of lowercase characters. 
The task is to check whether two given strings are anagram of each other or not. 
An anagram of a string is another string that contains same characters, 
only the order of characters can be different. For example, “act” and “tac” are anagram of each other.

Input:
The first line of input contains an integer T denoting the number of test cases. 
Each test case consist of two strings in 'lowercase' only, in a single line.

Output:
Print "YES" without quotes if the two strings are anagram else print "NO".

Constraints:
1 ≤ T ≤ 300
1 ≤ |s| ≤ 106

Example:
Input:
2
geeksforgeeks forgeeksgeeks
allergy allergic

Output:
YES
NO

Explanation:
Testcase 1: Both the string have same characters with same frequency. So, both are anagrams.
Testcase 2: Characters in both the strings are not same, so they are not anagrams.
*/

# include <stdio.h>

int strLen(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++);
    return i;
}

char *func(char *str1, int n1, char *str2, int n2){
    int i, balance=0;

    for(i=0; i<n1; i++)
        balance += str1[i];
    for(i=0; i<n2; i++)
        balance -= str2[i];
    
    if(balance == 0)
        return "YES";
    else
        return "NO";
}

int main(){
    int t;
    char arr1[32], arr2[32];

    scanf("%d", &t);
    while(t>0){
        scanf("%s", &arr1);
        scanf("%s", &arr2);
        printf("OP : %s\n",func(arr1, strLen(arr1), arr2, strLen(arr2)));
        t -= 1;
    }

    return 0;
}