/*
Given two arrays X and Y of positive integers,
find number of pairs such that x^y > y^x (raised to power of) where x is an element from X and y is an element
from Y.

Input:
The first line of input contains an integer T, denoting the number of test cases.
Then T test cases follow. Each test consists of three lines.
The first line of each test case consists of two space separated M and N denoting size of arrays X and Y
respectively. The second line of each test case contains M space separated integers denoting
the elements of array X. The third line of each test case contains N space separated integers denoting
elements of array Y.

Output:
Corresponding to each test case, print in a new line, the number of pairs such that x^y > y^x.

Constraints:
1 ≤ T ≤ 100
1 ≤ M, N ≤ 105
1 ≤ X[i], Y[i] ≤ 103

Example:
Input
1
3 2
2 1 6
1 5

Output
3

Explanation:
Testcase 1: The pairs which follow x^y > y^x are as such: 2^1 > 1^2,  2^5 > 5^2 and 6^1 > 1^6
*/
# include <stdio.h>

int pow_(int b, int e){
    if(e == 0)
        return 1;
    else if(e == 1)
        return b;
    else
        return b*pow_(b,e-1);
}

int func(int *arr_n, int n, int *arr_m, int m){
    int i, j, count=0;

    for(i=0; i<n; i++)
        for(j=0; j<m; j++)
            if(pow_(arr_n[i],arr_m[j]) > pow_(arr_m[j],arr_n[i]))
                count++;

    return count;
}

int main(){
    int t, n, m, arr_n[25], arr_m[25], i;

    scanf("%d", &t);
    if(t>=1 && t<=100)
        while(t>0){
            scanf("%d%d", &n, &m);
            if(n>=1 && n<=107){
                for(i=0; i<n; i++)
                    scanf("%d", &arr_n[i]);
                for(i=0; i<m; i++)
                    scanf("%d", &arr_m[i]);
                printf("OP : %d", func(arr_n, n, arr_m, m));
            }
            t -= 1;
        }

    return 0;
}