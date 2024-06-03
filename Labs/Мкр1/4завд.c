#include <stdio.h>
#include <math.h>

int main() {
  double a, b, c, S;

  printf("Введіть катет a: ");
  scanf("%lf", &a);

  printf("Введіть катет b: ");
  scanf("%lf", &b);

  c = sqrt(a * a + b * b);

  S = 0.5 * a * b;

  printf("Гіпотенуза c = %lf\n", c);
  printf("Площа S = %lf\n", S);

  return 0;
}
