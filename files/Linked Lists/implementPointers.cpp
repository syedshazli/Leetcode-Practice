#include <stdio.h>
#include <iostream>
using namespace std;
int main(){
    int find = 38;
    int *pointToFind = &find;

    cout<<"Variable has a value of "<<find<<endl;
    cout<<"Memory address of variable is "<<&find<<endl;

    cout<<"I have a pointer called pointToFind, pointing to find. It has a memory address of "
    <<pointToFind<< " same as memory address of my variable"<<endl;

    cout<<"My pointer dereferenced should have the same value as find. It's value is "<<*pointToFind<<endl;

}
