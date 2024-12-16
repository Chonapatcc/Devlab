#include <iostream>
#include <vector>
using namespace std;

vector<long long int> store;

long long int factorial(long long int a)
{
    if(store[a])
    {
        return a;
    }

    if(a==1)
    {
        store[a] = 1;
        return 1;
    }
    
    return a * factorial(a-1);
}

int main()
{
    long long int a ; 
    cin >> a;
    store = vector<long long int> (a+1);
    cout << factorial(a) << endl;
}