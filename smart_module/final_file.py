# Импорт переменных из разных файлов
from src.features.string_concatenation import nested_variable_string_1 as string_var_1
from src.utils.comma_concatenation import nested_variable_comma_1 as comma_var_1
from src.formatting.format_method import nested_variable_format_1 as format_var_1
import src.formatting.percent_format as percent_format_module
import src.formatting

# Переопределение значения через input()
nested_variable_main_1 = input()

# Переопределение значения через импорт (string_var_1)
# False - значение теперь импортируется
nested_variable_main_2 = string_var_1

# Переопределение значения через импорт (comma_var_1)
# False - значение теперь импортируется
nested_variable_main_3 = comma_var_1

# Использование форматирования из percent_format_module
# True used_in_percent
nested_variable_main_4 = percent_format_module.nested_variable_percent_1

# import src.formatting.percent_format as percent_format_module
nested_variable = percent_format_module.nested_variable_percent_2
nested_variable__NEW = f'my current_var is: {percent_format_module.nested_variable_percent_3}'
variable_with_big_import_line = formatting