#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int h=0;
struct node 
{ 
	char data; 
	struct node* left; 
	struct node* right; 
}; 
struct node* newNode(char data) 
{ 
	struct node* node = (struct node*) 
	malloc(sizeof(struct node)); 
	node->data = data; 
	node->left = NULL; 
	node->right = NULL; 
	return(node); 
}
/* Given a binary tree, print its nodes in postorder*/
void printPostorder(struct node* node){ 
	if (node == NULL) 
		return; 
	// first recur on left subtree 
	printPostorder(node->left); 
	
	// then recur on right subtree 
	printPostorder(node->right); 
	
	// now deal with the node 
	printf("%c ", node->data); 
} 
  
/* Given a binary tree, print its nodes in inorder*/
void printInorder(struct node* node){ 
	if (node == NULL) 
		return; 
	
	/* first recur on left child */
	printInorder(node->left); 
	
	/* then print the data of node */
	printf("%c ", node->data);   
	
	/* now recur on right child */
	printInorder(node->right); 
}

/* Given a binary tree, print its nodes in preorder*/
void printPreorder(struct node* node){ 
	if (node == NULL) 
		return; 
	
	/* first print data of node */
	printf("%c ", node->data);   
	
	/* then recur on left sutree */
	printPreorder(node->left);   
	
	/* now recur on right subtree */
	printPreorder(node->right); 
}
void clearArray(char array[]){
	int i = 0;
	while(array[i] != '\0'){
		array[i] = '\0';
		i++;
	}
	i = 0;
}

void printArray(char array[]){
	int i = 0;
	while(array[i] != '\0'){
		printf("%c",array[i]);
		i++;
	}
}

void PrintCharToMorse(struct node* node,char c,char morseCode[],int i) 
{
	
	if (node == NULL) 
		return;
	if (node->data == c){
		morseCode[i] = ' ';
		printArray(morseCode);
		clearArray(morseCode);
		return;
	}
	
	
	//Left Recur
	morseCode[i] = '.';
	i++;
	PrintCharToMorse(node->left,c,morseCode,i);
	i--;
	morseCode[i] = '\0';
	
	//Right Recur
	morseCode[i] = '-';
	i++;
	PrintCharToMorse(node->right,c,morseCode,i);
	i--;
	morseCode[i] = '\0';
}


void PrintMorseToString(struct node* node ,char morseCode[]){
	
	
	struct node *letter = node;
	int i = 0;
	
	
	while(morseCode[i] != '\0'){ //Adding a space at the end of the string
		i++;
	}
	
	
	morseCode[i] = ' ';
	i=0;
	while(morseCode[i] != '\0'){
		
		if(morseCode[i] == '\0')
			printf("%c",letter->data);
			
		if(morseCode[i]==' '){
			printf("%c",letter->data);
			if(morseCode[i+1] == ' '){
				printf(" ");
			}
			letter = node;
		}
			
		if(morseCode[i]=='.'){
			letter = letter->left;
		}
		
		if(morseCode[i]=='-'){
			letter = letter->right;
		}
		i++;
	}
	if(morseCode[i+1] == '\0')
		printf("%c",letter->data);
		
	if(morseCode[i+1]==' '){
		printf("%c",letter->data);
		letter = node;
	}
		
		
	if(morseCode[i+1]=='.'){
		letter = letter->left;
	}
	
	if(morseCode[i+1]=='-'){
		letter = letter->right;
	}
}

int main() 
{ 


	int b = 0;
	char morseCode[255];
	char stri[255];
	char morseArray[255];
	morseArray[0] = 'a';
	morseArray[1] = 'b';
	
	
	printArray(morseArray);
	clearArray(morseArray);
	printArray(morseArray);
	
	
	struct node *root   = newNode(' ');	
	
	//Parent: ROOT 
	root->left          = newNode('E'); 
	root->right         = newNode('T');
	//Parent: E
	root->left->left    = newNode('I'); 
	root->left->right   = newNode('A');
	//Parent: T
	root->right->left   = newNode('N');
	root->right->right  = newNode('M');
	//Parent: I
	root->left->left->left     = newNode('S');
	root->left->left->right    = newNode('U');
	//Parent: A
	root->left->right->left    = newNode('R');
	root->left->right->right   = newNode('W');
	//Parent: N
	root->right->left->left    = newNode('D');
	root->right->left->right   = newNode('K');
	//Parent: M
	root->right->right->left   = newNode('G');
	root->right->right->right  = newNode('O');
	//Parent: S
	root->left->left->left->left     = newNode('H');
	root->left->left->left->right     = newNode('V');
	//Parent: U
	root->left->left->right->left    = newNode('F');
	//Parent: R
	root->left->right->left->left    = newNode('L');
	//Parent: W
	root->left->right->right->left   = newNode('P');
	root->left->right->right->right   = newNode('J');
	//Parent: D
	root->right->left->left->left   = newNode('B');
	root->right->left->left->right    = newNode('X');
	//Parent: K
	root->right->left->right->left   = newNode('C');
	root->right->left->right->right   = newNode('Y');
	//Parent: G
	root->right->right->left->left   = newNode('Z');
	root->right->right->left->right   = newNode('Q');
	
	
	printf("Preorder:\n"); 
	printPreorder(root);
	printf("\n"); 
	
	printf("\nInorder:\n"); 
	printInorder(root);
	printf("\n"); 
	
	printf("\nPostorder:\n"); 
	printPostorder(root);
	printf("\n");
	
	
	
	printf("\nEnter The MORSECODE to Translate to STRING:\n");
	gets(morseCode);
	PrintMorseToString(root, morseCode);
	
	
	printf("\nEnter The STRING to Translate to MORSECODE:\n");
	gets(stri);
	while(stri[b] != '\0'){
		PrintCharToMorse(root,stri[b],morseArray,0);
		b++;
	}

	getchar(); 
	return 0; 
}
