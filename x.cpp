#include <bits/stdc++.h>
using namespace std;

int main()
{
    double s=0;
    int c;
    cin>>c;
    double num;
    for(int i=0; i<c; i++)
    {
        cin>>num;
        s+=num;
    }
    
    cout <<fixed<<setprecision(1) <<s/c<<endl;
}