#include <stdio.h>

double sum(double numbers[], int size) {
  double total = 0;
  for (int i = 0; i < size; i++) {
    total += numbers[i];
  }
  return total;
}

int main() {
  int n;
  double numbers[n];
  printf("Введіть натуральне число п: ");
  scanf("%d", &n);
  printf("Введіть дійсні числа: ");
  for (int i = 0; i < n; i++) {
    scanf("%lf", &numbers[i]);
  }
  double result = sum(numbers, n);
  printf("Сума чисел дорівнює %1f\n", result);
  return 0;
}
