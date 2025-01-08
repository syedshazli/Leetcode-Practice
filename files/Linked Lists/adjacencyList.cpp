// to compile (linux): 
//  1. g++ AdjacencyMatrix.cpp -o AdjacencyMatrix
//  2. ./AdjacencyMatrix
//  3. Enter number of nodes in your graph
//  4. Enter number of edges in your graph
//  5. Start listing start nodes and end nodes in an edge
//  6. View finalised Adjacency List
#include <vector>
#include <stdio.h>
#include <iostream>
using namespace std;

int main(){
    int numNodes;
    cout<<"Please enter how many nodes are in your graph."<<endl;
    cin>>numNodes;

    int numEdges;
    cout<<"Please enter how many edges are contained in your graph"<<endl;
    cin>>numEdges;
    //initialise adjacency matrix as array of arrays
    //node number as row, connections as column (?)
    vector< vector< int> > graph(numNodes, vector<int>());

    //connection from u->v
    int u;
    int v;

    for (int i = 0; i< numEdges; i++){
        cout<<"Please enter a edge separated by input. So if there is an edge from x (starting node) to y (ending node), please enter x then enter y"<<endl;
        cin>>u;
        cin>>v;
        graph[u].push_back(v); //in the array containing edges for 'u', add the edge 'v' to the list
    }

    // add node
    graph.push_back(vector<int>());

    //todo: print our graph
    int index = 0;
    for(auto z: graph){
        cout<<index<<"-->";
        for(auto y:z){
            cout<<y<<", ";
        }
        index+=1;
        cout<<endl;
    }

}//end of main
