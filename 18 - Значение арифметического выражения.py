def evaluate_expression(expression):
    try:
        # Удаляем пробелы из выражения
        cleaned_expression = expression.replace(" ", "")
        
        # Проверка на некорректные пробелы между числами
        import re
        if re.search(r'\d\s+\d', expression):
            print("WRONG")
            return
        
        # Пытаемся вычислить значение выражения
        result = eval(cleaned_expression)
        
        # Проверяем, что результат является целым числом и входит в допустимые пределы
        if isinstance(result, int) and abs(result) <= 2 * 10**9:
            print(result)
        else:
            print("WRONG")
    except:
        # Если возникла любая ошибка, выводим "WRONG"
        print("WRONG")

# Чтение входного выражения
expression = input().strip()

# Вычисление значения выражения
evaluate_expression(expression)
