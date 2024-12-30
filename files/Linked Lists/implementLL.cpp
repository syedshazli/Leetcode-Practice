#include <stdio.h>
#include <iostream>
using namespace std;


    struct node{
        int data;
        node* next;
    };

int main(){
    //initalise 3 nodes
    node* n;
    node* temporary;
    node* head;

    //set n to be a new node in order to allow us to change what n is pointing to
    n = new node;
    n->data = 1;

    temporary = n;
    head = n;

    n = new node;
    n->data = 2;

    temporary->next = n;
    temporary = temporary->next;

    n = new node;
    n->data = 3;

    //where the next part of temp needs to point to (the node n is pointing to)
    temporary->next = n;

    n = new node;
    //make temp point to temps next element
    temporary = temporary->next;

    n->data = 4;
    temporary->next = n;

    //end of list
    n->next = nullptr;
    

}
