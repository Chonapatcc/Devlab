#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int num ;
    cin>>num;
    vector<bool> is_prime(num + 1, true);
    vector<int> prime_numbers;
    is_prime[0] = is_prime[1] = false; // 0 and 1 are not prime numbers

    for(int p = 2; p * p <= num; p++)
    {
        if(is_prime[p])
        {
            for(int multiple = p * p; multiple <= num; multiple += p)
            {
                is_prime[multiple] = false;
            }
        }
    }
    for(int i = 2; i <= num; i++)
    {
        if(is_prime[i])
        {
            prime_numbers.push_back(i);
        }
    }

    if(is_prime[num])
    {
        cout << prime_numbers.size() << endl;
    }
    else
    {
        cout << prime_numbers.back() << endl;
    }
}