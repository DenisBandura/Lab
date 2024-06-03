import math

def calculate_square_root(x, a):

  if x < 0:
    raise ValueError("Не можна обчислити квадратний корінь негативного числа.")

  if a == 0:
    return 1

  # Обчислюємо квадратний корінь x
  square_root = math.sqrt(x)

  # Підносимо квадратний корінь x до степеня a
  result = square_root ** a

  return result

x = 5
y = 3
a = 2

# Обчислюємо квадратний корінь x, піднятого до степеня a
result = calculate_square_root(x, a)

print(f"Result: {result}")  # Output: 1.5384615384615385
