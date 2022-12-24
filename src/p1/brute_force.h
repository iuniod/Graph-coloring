// C++ program for solution of M
// Coloring problem using backtracking

#include <bits/stdc++.h>
using namespace std;

bool isSafe(int v, map<int, vector<int>> graph, int color[], int c) {
	for (auto i : graph[v]) {
		if (c == color[i])
			return false;
	}

	return true;
}

/* A recursive utility function
to solve m coloring problem */
bool graphColoringUtil(map<int, vector<int>> graph, int n, int m, int color[], int v) {
	if (v == n)
		return true;

	for (int c = 1; c <= m; c++) {
		if (isSafe(v, graph, color, c)) {
			color[v] = c;

			if (graphColoringUtil(graph, n, m, color, v + 1) == true)
				return true;

			color[v] = 0;
		}
	}

	return false;
}

bool graphColoring(map<int, vector<int>> graph, int n, int m) {
	int color[n];
	for (int i = 0; i < n; i++)
		color[i] = 0;

	// Call graphColoringUtil() for vertex 0
	if (graphColoringUtil(graph, n, m, color, 0) == false) {
		return false;
	}

	return true;
}

int chNo_BruteForce(map<int, vector<int>> graph, int n) {
	int m = 1;
	while (!graphColoring(graph, n, m)) {
		m++;
	}

	return m;
}

// This code is contributed by Shivani
