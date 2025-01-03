# Получаем значение через input()
current_variable_comma_1 = input()
current_variable_comma_2 = input()
current_variable_comma_3 = input()
current_variable_comma_4 = input()
current_variable_comma_5 = input()

# True used_in_comma_concatenation
nested_variable_comma_1 = ("Значение: ", current_variable_comma_1)

# True used_in_comma_concatenation
nested_variable_comma_2 = ("Значение: ", current_variable_comma_2, "- это мое значение")

# True used_in_comma_concatenation
nested_variable_comma_3 = (current_variable_comma_3, "- это мое значение")

# False
nested_variable_comma_4 = (current_variable_comma_4)

# True used_in_comma_concatenation
nested_variable_comma_5 = ("Значение: ", "Другой текст", current_variable_comma_5)
