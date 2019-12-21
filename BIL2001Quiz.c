#include <stdio.h> 
#include <stdlib.h>
typedef struct node {
    int val;
    struct node * next;
}node_t;

//Prints the list until the las node is NULL
void printList(node_t * head) {
    node_t * current = head;

    while (current != NULL) {
        printf("%d->", current->val);
        current = current->next;
    }
    printf("\n");
}
//Prints the CYCLE list Once
void printOneCycle(node_t * head){
	node_t * current = head;
	printf("%d->",current->val);
	current = current->next;
    while (current != head) {
        printf("%d->", current->val);
        current = current->next;
    }
    printf("\n");
}

void AnnounceTheWinner(node_t * head){
	if(head->val == 1)
		printf("%dst Soldier Won!",head->val);
	if(head->val == 2)
		printf("%dnd Soldier Won!",head->val);
	if(head->val == 3)
		printf("%drd Soldier Won!",head->val);
	if(head->val > 3)
		printf("%dth Soldier Won!",head->val);
}

//Connects the end of the list to the front
void makeCycle(head){
	node_t * current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = head;
    
}


//Start killing Soldiers
void StartKillingCoroutine(head){
	node_t * current = head;
    while (current != current->next->next) {
    	//printf("%d",current->val);
    	printf("%d\tKilled:       \t%d\n",current->val,current->next->val);
        current->next = current->next->next;
        current = current->next;
    }
    current->next = current;
    printf("\n");
    AnnounceTheWinner(current);
}

//Adds a NODE to the list
void push(node_t * head, int val){
	
    node_t * current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    //Add the new NODE
    current->next = malloc(sizeof(node_t));
    current->next->val = val;
    current->next->next = NULL;
}
int main() 
{
	int soldierCount;
	
	int i;
    node_t * head = NULL;
	head = malloc(sizeof(node_t));
	printf("Enter the Soldier Count:");
	scanf("%d",&soldierCount);
	if (head == NULL) {
		printf("Allocation failed...");;
	    return 1;
	}
	
	head->val = 1;
	head->next = NULL;
	
	for(i=2;i<=soldierCount;i++){
		push(head,i);
	}
	
	printList(head);
	makeCycle(head);
	StartKillingCoroutine(head);
}
