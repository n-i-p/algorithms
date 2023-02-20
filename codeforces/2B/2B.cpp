#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

#ifdef _DEBUG
#define cin f
ifstream f("tests/2B_01.in");
#endif

typedef struct trailing_zeros_and_last_digit { int tz, ld; } TzLd;

inline TzLd get_tzld(int number) {
	if (number == 0) {
		return TzLd{ 1, 0 };
	}
	int zeros = 0;
	while (number % 10 == 0) {
		zeros++;
		number /= 10;
	}
	return TzLd{ zeros, number % 10 };
}

void pm(int n, int** a) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << a[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

int main()
{
	int temp;
	int n;
	cin >> n;

	vector<vector<int>> a;
	vector<vector<int>> t;
	vector<vector<int>> l;
	vector<vector<char>> d;
	for (int i = 0; i < n; i++) {
		a.push_back(vector<int>());
		t.push_back(vector<int>());
		l.push_back(vector<int>());
		d.push_back(vector<char>());
		for (int j = 0; j < n; j++) {
			cin >> temp;
			a[i].push_back(temp);
			t[i].push_back(-1);
			l[i].push_back(-1);
			d[i].push_back('\0');
		}
	}

	/// int priorities[] = {1, 3, 7, 9, 4, 6, 8, 2, 5, 0};
	int priorities[] = { 9, 0, 7, 1, 4, 8, 5, 2, 6, 3 };

	for (int x = n - 1; x >= 0; x--) {
		for (int y = n - 1; y >= 0; y--) {
			if (x == n - 1 && y == n - 1) {
				TzLd tzld = get_tzld(a[x][y]);
				t[x][y] = tzld.tz;
				l[x][y] = tzld.ld;
			}
			else if (x == n - 1) {
				TzLd tzld = get_tzld(a[x][y] * l[x][y + 1]);
				d[x][y] = 'R';
				t[x][y] = t[x][y + 1] + tzld.tz;
				l[x][y] = tzld.ld;
			}
			else if (y == n - 1) {
				TzLd tzld = get_tzld(a[x][y] * l[x + 1][y]);
				d[x][y] = 'D';
				t[x][y] = t[x + 1][y] + tzld.tz;
				l[x][y] = tzld.ld;
			}
			else {
				int nx, ny;
				char nd;
				if (t[x][y + 1] == t[x + 1][y]) {
					TzLd tzldR = get_tzld(a[x][y] * l[x][y + 1]);
					TzLd tzldD = get_tzld(a[x][y] * l[x + 1][y]);
					if (priorities[tzldR.ld] < priorities[tzldD.ld]) {
						nx = x;
						ny = y + 1;
						nd = 'R';
					}
					else {
						nx = x + 1;
						ny = y;
						nd = 'D';
					}
				}
				else if (t[x][y + 1] < t[x + 1][y]) {
					nx = x;
					ny = y + 1;
					nd = 'R';
				}
				else if (t[x][y + 1] > t[x + 1][y]) {
					nx = x + 1;
					ny = y;
					nd = 'D';
				}
				else {
					return 10;
				}
				TzLd tzld = get_tzld(a[x][y] * l[nx][ny]);
				d[x][y] = nd;
				t[x][y] = t[nx][ny] + tzld.tz;
				l[x][y] = tzld.ld;
			}
		}
	}

	vector<char> directions;
	int x = 0;
	int y = 0;
	int pos = 0;
	while (x != n - 1 || y != n - 1) {
		directions.push_back(d[x][y]);
		if (d[x][y] == 'R') {
			y++;
		}
		else if (d[x][y] == 'D') {
			x++;
		}
		else if (d[x][y] == 0) {
			break;
		}
		else {
			return 20;
		}
	}
	cout << t[0][0] << endl;
	for (char c : directions) {
		cout << c;
	}
	cout << endl;

	ofstream g("t.out");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			g << t[i][j] << " ";
		}
		g << endl;
	}

	return 0;
}
