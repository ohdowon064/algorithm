#include <iostream>
#include <vector>
#include <algorithm>
#define all(v) (v).begin(), (v).end()
using namespace std;
typedef long long ll;
const int MAX = 300001;
vector<int> v[MAX];
ll N, d[MAX], ans;

ll ret(ll n) {
	return n * (n - 1) / 2;
}

ll dfs(int cur) {
	d[cur] = 1;
	for (auto i : v[cur]) {
		if (!d[i]) {
			d[cur] += dfs(i);
		}
	}
	ans += ret(N) - ret(N - d[cur]);
	return d[cur];
}

int main() {
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	cin >> N;
	for (int i = 0; i < N - 1; i++) {
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	dfs(1);
	cout << ans - ret(N) << "\n";
}