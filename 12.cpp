#include <bits/stdc++.h>
using namespace std;

int main()
{
    string s, ans = "";
    cin >> s;
    vector<int> v(26, 0);
    int cnt = 0;
    for (char &c : s)
    {
        if (v[c - 'A'] == 0)
        {
            cnt++;
            v[c - 'A'] = 1;
        }
        else
        {
            cnt--;
            v[c - 'A'] = 0;
            ans += c;
        }
    }
    if (cnt > 1)
    {
        cout << "NO SOLUTION" << endl;
        return 0;
    }
    cout << ans;
    for (char c = 'A'; c <= 'Z'; c++)
    {
        if (v[c - 'A'] == 1)
        {
            cout << c;
        }
    }
    reverse(ans.begin(), ans.end());
    cout << ans;
    return 0;
}