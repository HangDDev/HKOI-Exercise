// https://judge.hkoi.org/task/D101

#include <iostream>
using namespace std;

int main() {
  string num;
  cin >> num;
  
  if (num.rfind("2", 0) == 0 or num.rfind("3", 0) == 0) {
    cout << "Fixed";
  } else {
    cout << "Mobile";
  }
}
