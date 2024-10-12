// https://judge.hkoi.org/task/D111
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  float w, h, bmi = 0;
  cin >> w >> h;
  bmi = w / (h*h);
  cout << fixed << setprecision(3) << bmi << endl;
  if (bmi < 18.5) {
    cout << "Underweight" << endl;
  } else if (bmi >= 18.5 and bmi < 23) {
    cout << "Normal" << endl;
  } else if (bmi >= 23 and bmi < 25) {
    cout << "Overweight" << endl;
  } else if (bmi >= 25) {
    cout << "Obese" << endl;
  }
}
