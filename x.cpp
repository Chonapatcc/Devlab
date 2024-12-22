#include <bits/stdc++.h>
using namespace std;

int main()
{
    string t;
    vector<string> v;
    while(cin >> t)
    {
        v.push_back(t);
    }
    int p = 0;
    cout << '[';
    for(int i = v.size()-1 ; i >= 0 ; i--)
    {
        for(char c: v[i])
        {
            if(p)
            {
                cout<<',' ;
            }
            else
            {
                p = 1;
            }
            cout << c;
        }
    }
    cout << ']';
    return 0;
}