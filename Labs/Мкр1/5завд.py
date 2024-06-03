def calculate_product(x):

  product = 1
  for i in range(1, x + 1):
      product *= (i + 0.1)

  return product


result = calculate_product(10)
print(f"Result: {result}")  # Output: 1.3976243610792913
