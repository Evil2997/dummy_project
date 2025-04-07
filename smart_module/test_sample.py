# test_sample.py

TARGET_VAR = input()
from project.SubDir.exotic import current_var

def test_function():
    # Прямое использование глобальной переменной
    print("TARGET_VAR:", TARGET_VAR)

    # Присваивание: новая переменная получает значение TARGET_VAR
    new_message = TARGET_VAR + " - processed"

    # Вложенная функция, использующая TARGET_VAR
    def inner_function():
        # Использование TARGET_VAR внутри вложенной функции
        def third_lvl():
            # a = current_var
            return current_var
        modified = TARGET_VAR.upper() + third_lvl()
        return f"Inner: {modified}"

    # Lambda-выражение, использующее TARGET_VAR
    lambda_result = (lambda suffix: TARGET_VAR + suffix)("!!!")
    result = eval(TARGET_VAR)
    # Результаты работы вложенной функции и lambda
    inner_result = inner_function()
    print("Inner function result:", inner_result)
    print("Lambda result:", lambda_result)
    eval_result = result
    return new_message, eval_result


if __name__ == '__main__':
    final_message, result_with_eval = test_function()
    print("Final message:", final_message)
