/*
Given a singly linked list of N nodes. The task is to find middle of the linked list. 
For example, if given linked list is 1->2->3->4->5 then output should be 3.
If there are even nodes, then there would be two middle nodes, we need to print second middle element. 
For example, if given linked list is 1->2->3->4->5->6 then output should be 4.

Input:
First line of input contains number of testcases T. For each testcase, 
first line of input contains length of linked list and next line contains data of nodes of linked list.

Output:
For each testcase, there will be a single line of output containing data of middle element of linked list.

User Task:
The task is to complete the function getMiddle() which takes head reference as the only argument 
and should return the data at the middle node of linked list.

Constraints:
1 <= T <= 100
1 <= N <= 100

Example:
Input:
2
5
1 2 3 4 5
6
2 4 6 7 5 1

Output:
3
7

Explanation:
Testcase 1: Since, there are 5 elements, therefore 3 is the middle element at index 2 (0-based indexing).
*/
# include <stdio.h>
#include <stdlib.h>

typedef struct LINKED_LIST{
    int data;
    int key;
    struct LINKED_LIST *link;    
}list;

int func(list **L, int n){
    list *head = *L;
    n = n/2 + 1;
    while(head->link != NULL){
        if(head->key == n)
            return head->data;
        head = head->link;
    }
}

void append_node(list **head, int data, int key){

    list *new_node = (list*)malloc(sizeof(list));
    list *last = *head;

    new_node->data = data;
    new_node->key = key+1;
    new_node->link = NULL;

    if(*head == NULL) { 
       *head = new_node; 
       return; 
    }   
    while(last->link != NULL) 
        last = last->link;
   
    last->link = new_node;
    return;
}

void printList(list *node)
{
    while (node != NULL){
        printf("[%d] ", node->data);
        node = node->link;
    }
    printf("\n");
}

int main(){
    int t, n, i, temp;
    list *L = NULL;

    scanf("%d", &t);
    while(t>0){
        L = NULL;
        scanf("%d", &n);
        for(i=0; i<n; i++){
            scanf("%d", &temp);
            append_node(&L, temp, i);
        }
        // printList(L);
        printf("OP : %d\n", func(&L, n));
        t--;
    }

    return 0;
}