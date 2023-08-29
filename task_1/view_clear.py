

def convert_to_expected_type(value, expected_type): # Конвертация в ожидаемый тип
    try:
        return expected_type(value) #Kонвертируем
    except (ValueError, TypeError) as e: # Если ошибка, то печатаем ее и пропускаем значение
        print(e)
        return value
