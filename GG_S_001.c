/*
Given a String of length S, reverse the whole string without reversing the individual words in it.
Words are separated by dots.

Input:
The first line contains T denoting the number of testcases.
T testcases follow.
Each case contains a string S containing characters.

Output:
For each test case, in a new line, output a single line containing the reversed String.

Constraints:
1 <= T <= 100
1 <= |S| <= 2000

Example:
Input:
2
i.like.this.program.very.much
pqr.mno

Output:
much.very.program.this.like.i
mno.pqr
*/
# include <stdio.h>

int strLen(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++);
    return i;
}

void func(char *arr, int len){
    int head=len, tail=len, i, j;
    for(i=len-1; i>=-1; i--){
        if((arr[i] == '.' && i != head) || i == -1){
            head = i+1;
            for(j=head; j<tail; j++)
                printf("%c", arr[j]);
            if(i != -1)
                printf(".");
            tail = i;
        }
    }
    printf("\n");
}

int main(){
    int t;
    char arr[1024];

    scanf("%d", &t);
    if(t>=1 && t<=100){
        while (t>0){
            scanf("%s", &arr);
            printf("OP : ");
            func(arr, strLen(arr));
            t -= 1;
        }
    }
    return 0;
}