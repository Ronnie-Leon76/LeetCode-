#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

pair<int, int> dir[4] = { {1,0}, {0,1},{-1,0},{0,-1} };

bool check(vector<vector<char>> &mat, vector<vector<bool>> &vis,int row,int col) {
    // Check if the cell has been visited and check the size of the row and column
	if (row >= 0 && row < mat.size() && col >= 0 && col < mat[0].size() && mat[row][col]=='.' &&  !vis[row][col]) {
		return true;}
	return false;
}

int bfs(vector<vector<char>> &mat, vector<vector<bool>> &vis, vector<pair<int,int>> &special) {
	queue<pair<int,int>> que;
	for (int i = 0; i < special.size(); i++) que.push(special[i]);
	int res=0;
	int path=0;
	while (que.size()) {
		int size = que.size();
		for (int j = 0; j < size; j++) {
			res += path;
			pair<int, int> point = que.front();
			que.pop();
			for (int i = 0; i < 4; i++) {
				int row = point.first + dir[i].first;
				int col = point.second + dir[i].second;
				if (check(mat, vis, row, col)) {
					que.push({ row, col });
					vis[row][col] = true;
				}
			}
		}
		path++;
	}
	return res;
}

int main() {
	int N, M, K;
	int specialX, specialY;
	char element;

	cin >> N >> M >> K;
	// Character matrix
	vector<vector<char>> mat(N, vector<char>(M));
	// Visited cells boolean matrix
	vector<vector<bool>> vis(N, vector<bool>(M));
	vector<pair<int, int>> special(K);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> element;
			mat[i][j] = element;
		}
	}
	for (int i = 0; i < K; i++) {
		cin >> specialX;
		cin >> specialY;
		special[i].first = specialX - 1;
		special[i].second = specialY - 1;
		vis[special[i].first][special[i].second] = true;
	}
	
	cout<<bfs(mat, vis, special)<<endl;

	return 0;
}