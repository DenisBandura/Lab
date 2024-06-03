def count_negatives(arr, n):
  """
  Функція підрахунку кількості від'ємних елементів у масиві.

  Args:
    arr: Масив цілих чисел.
    n: Розмір масиву.

  Returns:
    Кількість від'ємних елементів у масиві.
  """
  count_negatives = 0
  for i in range(n):
    if arr[i] < 0:
      count_negatives += 1
  return count_negatives

def read_array(arr, n):
  """
  Функція читання масиву з вводу користувача.

  Args:
    arr: Масив цілих чисел.
    n: Розмір масиву.
  """
  for i in range(n):
    arr[i] = int(input(f"Введіть елемент {i + 1}: "))

def print_array(arr, n):
  """
  Функція виведення масиву на екран.

  Args:
    arr: Масив цілих чисел.
    n: Розмір масиву.
  """
  for i in range(n):
    print(arr[i], end=" ")
  print()

if __name__ == "__main__":
  n = int(input("Введіть розмір масивів: "))
  a = [0] * n
  b = [0] * n

  read_array(a, n)
  read_array(b, n)

  a_negatives = count_negatives(a, n)
  b_negatives = count_negatives(b, n)

  if a_negatives > b_negatives:
    print("Масив а має більше від'ємних елементів.")
  elif a_negatives < b_negatives:
    print("Масив в має більше від'ємних елементів.")
  else:
    print("Масиви а та в мають однакову кількість від'ємних елементів.")
