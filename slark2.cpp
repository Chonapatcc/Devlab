#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
    string reward1, front3_1, front3_2, back3_1, back3_2, back2, my_ticket;

    cin >> reward1 >> front3_1 >> front3_2 >> back3_1 >> back3_2 >> back2 >> my_ticket;

    int win_count = 0;
    double total_win = 0;

    if (my_ticket == reward1) {
        win_count++;
        total_win += 6000000;
    }
    if (my_ticket.substr(0, 3) == front3_1 ) {
        win_count++;
        total_win += 4000;
    }
    if (my_ticket.substr(0, 3) == front3_2) {
        win_count++;
        total_win += 4000;
    }

    if (my_ticket.substr(my_ticket.length() - 3) == back3_1 ) {
        win_count++;
        total_win += 4000;
    }
    if ( my_ticket.substr(my_ticket.length() - 3) == back3_2) {
        win_count++;
        total_win += 4000;
    }

    if (my_ticket.substr(my_ticket.length() - 2) == back2) {
        win_count++;
        total_win += 2000;
    }

    if (win_count == 0) {
        cout << "Better luck next time..." << endl;
    } else {
        double tax = total_win * 0.07;
        double net_win = total_win - tax;
        cout << "You win " << win_count << " " << (win_count == 1 ? "price." : "prices") << endl;
        cout << fixed << setprecision(0) << "Total = " << total_win << " THB" << endl;  // Use fixed and setprecision
        cout << fixed << setprecision(2) << "TAX 7 percents = " << tax << " THB" << endl; // Use fixed and setprecision
        cout << fixed << setprecision(2) << "You got " << net_win << " THB" << endl; // Use fixed and setprecision
    }

    return 0;
}