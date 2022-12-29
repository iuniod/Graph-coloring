// RLF Algorithm Graph Coloring
#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            a[i][j] = 0;

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        a[x][y] = 1;
        a[y][x] = 1;
    }

    int color[n];
    for (int i = 0; i < n; i++)
        color[i] = 0;

    color[0] = 1;
    int k = 1;
    while (k < n) {
        int c = 1;
        while (c <= n) {
            int flag = 0;
            for (int i = 0; i < n; i++) {
                if (a[k][i] == 1 && color[i] == c) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                color[k] = c;
                break;
            }
            c++;
        }
        k++;
    }
    int chromatic = 0;
    for (int i = 0; i < n; i++)
        if (color[i] > chromatic)
            chromatic = color[i];
    cout << chromatic << endl;
    return 0;
}