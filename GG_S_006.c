/*
Given an string in roman no format (s)  your task is to convert it to integer .

Input:
The first line of each test case contains the no of test cases T.
Then T test cases follow. Each test case contains a string s denoting the roman no.

Output:
For each test case in a new line print the integer representation of roman number s. 

Constraints:
1<=T<=100
1<=roman no range<4000

Example:
Input
2
V
III 
Output
5
3
*/

# include <stdio.h>

int strLen(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++);
    return i;
}

int value(char r)
{
    if (r == 'I')
        return 1;
    if (r == 'V')
        return 5;
    if (r == 'X')
        return 10;
    if (r == 'L')
        return 50;
    if (r == 'C')
        return 100;
    if (r == 'D')
        return 500;
    if (r == 'M')
        return 1000;

    return -1;
}

int func(char *str, int n){
    int res = 0, i, s1, s2;
    for(i=0; i<n; i++)
    {
        s1 = value(str[i]);
        if(i+1 < n)
        { 
            s2 = value(str[i+1]);
            if(s1 >= s2)
                res += s1;
            else{ 
                res += s2 - s1; 
                i++;
            } 
        } 
        else
            res = res + s1;
    }

    return res;
}

int main(){
    int t;
    char arr[24];

    scanf("%d", &t);
    while(t>0){
        scanf("%s", &arr);
        printf("OP : %d\n",func(arr, strLen(arr)));
        t -= 1;
    }

    return 0;
}