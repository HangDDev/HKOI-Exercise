// https://judge.hkoi.org/task/D106

#include <iostream>
using namespace std;

int main() {
  int n;
  string suffix;
  cin >> n;
  if (n % 100 >= 11 && n % 100 <= 13) {
    suffix = "th";
  } else {
    switch (n % 10) {
      case 1: suffix = "st"; break;
      case 2: suffix = "nd"; break;
      case 3: suffix = "rd"; break;
      default: suffix = "th"; break;
    }
  }
  cout << n << suffix << endl;
  return 0;
}
