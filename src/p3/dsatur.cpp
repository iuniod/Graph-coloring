// A C++ program to implement the DSatur algorithm for graph
// coloring

#include <iostream>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

// Struct to store information
// on each uncoloured vertex
struct nodeInfo {
	int sat; // Saturation degree of the vertex
	int deg; // Degree in the uncoloured subgraph
	int vertex; // Index of vertex
};
struct maxSat {
	bool operator()(const nodeInfo& lhs,
					const nodeInfo& rhs) const {
		// Compares two nodes by
		// saturation degree, then
		// degree in the subgraph,
		// then vertex label
		return tie(lhs.sat, lhs.deg, lhs.vertex)
			> tie(rhs.sat, rhs.deg, rhs.vertex);
	}
};

// Class representing
// an undirected graph
class Graph {

	// Number of vertices
	int n;

	// Number of vertices
	vector<vector<int> > adj;

public:
	// Constructor and destructor
	Graph(int numNodes) {
		n = numNodes;
		adj.resize(n, vector<int>());
	}
	~Graph() { adj.clear(); }

	// Function to add an edge to graph
	void addEdge(int u, int v);

	// Colour the graph
	// using the DSatur algorithm
	int DSaturColoring();
};

void Graph::addEdge(int u, int v) {
	adj[u].push_back(v);
	adj[v].push_back(u);
}

// Assigns colors (starting from 0)
// to all vertices and
// prints the assignment of colors
int Graph::DSaturColoring() {
	int u, i;
	vector<bool> used(n, false);
	vector<int> c(n), d(n);
	vector<set<int> > adjCols(n);
	set<nodeInfo, maxSat> Q;
	set<nodeInfo, maxSat>::iterator maxPtr;

	// Initialise the data structures.
	// These are a (binary
	// tree) priority queue, a set
	// of colours adjacent to
	// each uncoloured vertex
	// (initially empty) and the
	// degree d(v) of each uncoloured
	// vertex in the graph
	// induced by uncoloured vertices
	for (u = 0; u < n; u++) {
		c[u] = -1;
		d[u] = adj[u].size();
		adjCols[u] = set<int>();
		Q.emplace(nodeInfo{ 0, d[u], u });
	}

	while (!Q.empty()) {

		// Choose the vertex u
		// with highest saturation
		// degree, breaking ties with d.
		// Remove u from the priority queue
		maxPtr = Q.begin();
		u = (*maxPtr).vertex;
		Q.erase(maxPtr);

		// Identify the lowest feasible
		// colour i for vertex u
		for (int v : adj[u])
			if (c[v] != -1)
				used[c[v]] = true;
        int size = used.size();
		for (i = 0; i < size; i++)
			if (used[i] == false)
				break;
		for (int v : adj[u])
			if (c[v] != -1)
				used[c[v]] = false;

		// Assign vertex u to colour i
		c[u] = i;

		// Update the saturation degrees and
		// degrees of all uncoloured neighbours;
		// hence modify their corresponding
		// elements in the priority queue
		for (int v : adj[u]) {
			if (c[v] == -1) {
				Q.erase(
					{ int(adjCols[v].size()),
					d[v], v });
				adjCols[v].insert(i);
				d[v]--;
				Q.emplace(nodeInfo{
					int(adjCols[v].size()),
					d[v], v });
			}
		}
	}

	// chromatic number
    int chromatic = 0;
    for (int i = 0; i < n; i++)
        chromatic = max(chromatic, c[i]);
    
    return chromatic + 1;
}

// Driver Code
int main() {
	int n, m;
    cin >> n >> m;
    Graph g(n);
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        g.addEdge(x, y);
    }

    cout << g.DSaturColoring() << endl;

	return 0;
}

// https://www.geeksforgeeks.org/dsatur-algorithm-for-graph-coloring/?ref=rp