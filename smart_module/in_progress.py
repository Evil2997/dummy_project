from path4.path3 import path3_module1
from path4.path3.path2 import path2_module1
from path4.path3.path2.path1 import (
    path1_module1 as module1,
    path1_module2 as module2,
)

module_variable = path2_module1.variable_3
formatted_variable = f"{path2_module1.variable_3} + FIND_THIS"
concatenated_variable = path2_module1.variable_3 + "FIND_THIS"
tuple_variable_explicit = (path2_module1.variable_3, "FIND_THIS")
tuple_variable_implicit = path2_module1.variable_3, "FIND_THIS"

first_path_variable = module1.variable_first
second_path_variable = module2.variable_sec
