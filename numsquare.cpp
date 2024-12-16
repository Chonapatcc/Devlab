#include <iostream>
using namespace std;

int main()
{
    int a;
    cin>>a;
    if(a<=0)
    {
        cout << "ERROR";
        return 0;
    }
    for(int i=0; i<a; i++)
    {
        for(int j=0; j<a; j++)
        {
            cout << a;
        }
        cout <<endl;
    }
}