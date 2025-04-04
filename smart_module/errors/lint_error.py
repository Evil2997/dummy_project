# lint_errors.py

# Ошибка: неиспользуемый импорт (unused import)
import math

# Ошибка: неиспользуемая переменная (unused variable)
unused_var = 123

# Ошибка: несовместимый тип (incompatible type)
x: int = "string"

# Ошибка: f-string без плейсхолдеров (redundant f-string)
f"Just a string"

# Ошибка: повторное определение переменной (redefinition)
a = 1; a = 2

# Ошибка: функция с неправильной аннотацией (возвращаемый тип не соответствует аннотации)
def func() -> int: return "wrong"
