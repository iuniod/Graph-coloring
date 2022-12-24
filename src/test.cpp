#include <iostream>
#include "p1/brute_force.h"
// Number of vertices in the graph
#define NMAX 2000

using namespace std;

int main(int argc, char **argv) {
    map<int, vector<int>> graph;

    // Read input
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

	// Function call
	cout << chNo_BruteForce(graph, n) << endl;

	return 0;
}