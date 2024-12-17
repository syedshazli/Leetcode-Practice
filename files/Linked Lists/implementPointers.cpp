#include <stdio.h>
#include <iostream>
using namespace std;
int main(){
    int find = 38;
    int *pointToFind = &find;

    int **pointerToPointer = &pointToFind;

    cout<<"Variable has a value of "<<find<<endl;
    cout<<"Memory address of variable is "<<&find<<endl;

    cout<<"I have a pointer called pointToFind, pointing to find. It has a memory address of "
    <<pointToFind<< " same as memory address of my variable"<<endl;

    cout<<"My pointer dereferenced should have the same value as find. It's value is "<<*pointToFind<<endl;

    cout<<"I made a pointer that points to PointToFind. It has a memory address of "<<pointerToPointer<<" and when dereferenced, the value is "<<*pointerToPointer<<" which is the memory address of the pointer I am pointing to"<<endl;

    cout<<"To dereference the value of the pointer I am pointing to, we need to use **. So the value of what my pointer is pointing to is "<<**pointerToPointer<<endl;
}
