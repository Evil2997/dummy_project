# Получаем значение через input()
current_variable_percent_1 = input()
current_variable_percent_2 = input()
current_variable_percent_3 = input()
other_variable_percent_5 = input()

# True used_in_percent
nested_variable_percent_1 = "Значение: %s" % current_variable_percent_1

# True used_in_percent
nested_variable_percent_2 = "%s - это мое значение" % current_variable_percent_2

# True used_in_percent
nested_variable_percent_3 = "%s, %d" % (current_variable_percent_2, current_variable_percent_3)

# False
nested_variable_percent_4 = "%s" % "Текст"

# False
nested_variable_percent_5 = "Значение: %s" % other_variable_percent_5

nested_variable = "absolutely clean"
