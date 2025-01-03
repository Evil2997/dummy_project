# Получаем значение через input()
current_variable_format_1 = input()
current_variable_format_2 = input()
current_variable_format_3 = input()
other_variable_format_5 = input()

# True used_in_format
nested_variable_format_1 = "Значение: {}".format(current_variable_format_1)

# True used_in_format
nested_variable_format_2 = "{} - это мое значение".format(current_variable_format_2)

# True used_in_format
nested_variable_format_3 = "{}, {}".format("Текст", current_variable_format_3)

# False
nested_variable_format_4 = "{}".format("Текст")

# False
nested_variable_format_5 = "Значение: {}".format(other_variable_format_5)
