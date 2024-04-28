def reverse_string_recursive(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return reverse_string_recursive(input_string[1:]) + input_string[0]


input_str = "Hello, world!"
reversed_str = reverse_string_recursive(input_str)
print("Зворотній напрямок рядка:", reversed_str)
