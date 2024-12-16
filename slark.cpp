#include <iostream>
using namespace std;

int getFirst3Num(int num)
{
    while(num>=1000)
    {
        num/=10;
    }
    return num; 
}

int getLast3Num(int num)
{
    return num%1000;
}

int getLast2Num(int num)
{
    return num%100;
}


int main()
{
    int n1,nf31,nf32,nb31,nb32,nb2 , num;
    cin>>n1>>nf31>>nf32>>nb31>>nb32>>nb2>>num;

    int money =0 ;
    int c =0 ;
    if(n1 == num)
    {
        money = 6000000;
        c++;
    }

    int count =0 ;
    int count2 = 0;
    if(getFirst3Num(num) == nf31) count++;
    if(getFirst3Num(num) == nf32) count++;
    if(getLast3Num(num) == nb31) count++;
    if(getLast3Num(num) == nb32) count++;
    
    if(getLast2Num(num) == nb2) count2++;

    money+= count * 4000 + count2 *2000 ; 
    c+= count + count2;
    

    if(c==0)
    {
        cout << "Better luck next time..." <<endl;
    }
    else
    {
        string x;
        if(c==1)
        {
            x= "";
        }
        else
        {
            x = "s";
        }
        double tax = money*0.07;
        printf("You win %d price" , c);
        cout << x << ".\n";
        printf("Total = %d THB\n" , money);
        printf("TAX 7 percents = %.2lf THB\n" , tax);
        double result = money - tax;

        printf("You got %.2lf THB\n", result);
    }

    

}