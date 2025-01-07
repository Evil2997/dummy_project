# Импорт переменных из разных файлов
from smart_module.path4.path3 import init_variable_init
from src.features.string_concatenation import nested_variable_string_1 as string_var_1
from src.utils.comma_concatenation import nested_variable_comma_1 as comma_var_1
from src.formatting.format_method import nested_variable_format_1 as format_var_1
import src.formatting.percent_format as percent_format_module

nested_variable_main_1 = input()

nested_variable_main_2 = string_var_1

nested_variable_main_3 = comma_var_1
nested_variable_main_4 = percent_format_module.nested_variable_percent_1

nested_variable = percent_format_module.nested_variable_percent_2


# nested_variable__NEW = f'my current_var is: {percent_format_module.nested_variable_percent_3}'


import path4.path3.path3_module1
import path4.path3.path2.path2_module1
import path4.path3.path2.path1.path1_module1
import path4.path3.path2.path1.path1_module2


a = path4.path3.path2.path2_module1.variable_3
b = f"{path4.path3.path2.path2_module1.variable_3} + FIND_THIS"
c = path4.path3.path2.path2_module1.variable_3 + "FIND_THIS"
D1 = (path4.path3.path2.path2_module1.variable_3, "FIND_THIS")
D2 = path4.path3.path2.path2_module1.variable_3, "FIND_THIS"

AA1 = path4.path3.path2.path1.path1_module1.variable_first
AA2 = path4.path3.path2.path1.path1_module2.variable_sec


variable_with_big_import_line = path4.path3.path3_module1.variable_4

variable_with_big_import_line_2 = path4.path3.path3_module1.variable_2

nested_init = init_variable_init
