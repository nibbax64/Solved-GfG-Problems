/*
Given a string, the task is to remove duplicates from it. 
Expected time complexity O(n) where n is length of input string and extra space O(1) under 
the assumption that there are total 256 possible characters in a string.

Note: that original order of characters must be kept same. 

Input:
First line of the input is the number of test cases T. 
And first line of test case contains a string.

Output: 
Modified string without duplicates and same order of characters.

Constraints: 
1 <= T <= 15
1 <= |string|<= 1000

Example:
Input:
2
geeksforgeeks
geeks for geeks

Output:
geksfor
geks for
*/

# include <stdio.h>

int strLen(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++);
    return i;
}

void func(char *str, int n){
    int i=0, j=0;
    short hash[256]={0};
    char temp;

    while(*(str+i)){ 
        // printf("%s\n", str);
        temp = *(str+i); 
        if (hash[temp] == 0){ 
            hash[temp] = 1; 
            *(str+j) = *(str+i); 
            j++;
        } 
        i++;
    }       
  
  
  *(str+j) = '\0';

    printf("%s", str);
}

int main(){
    int t;
    char arr[24];

    scanf("%d", &t);
    while(t>0){
        fflush(stdin);
        scanf("%[^\n]", &arr);
        printf("OP : ");
        func(arr, strLen(arr));
        printf("\n");

        t -= 1;
    }

    return 0;
}