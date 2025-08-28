#include <iostream>
#include <string>
using namespace std;

bool pa(const string& p) {
    int i = 0;
    int f = p.size() - 1;

    while (i < f) {
        if (tolower(p[i]) != tolower(p[f])) {
            return false; 
        }
        i++;
        f--;
    }
    return true; 
}

int main() {
    string p;
    cout << "Digite uma palavra: ";
    cin >> p;

    if (pa(p)) {
        cout << p << " e um palindromo!" << endl;
    } else {
        cout << p << " nao e um palindromo." << endl;
    }

    return 0;
}
