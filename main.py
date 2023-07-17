from openpyxl import load_workbook

# Загрузка книги Excel
workbook = load_workbook(r"C:\Users\1\Downloads\sber_pd4.xlsx")

# Получение активного листа
sheet = workbook.active

# Обновление значения ячейки, на которую ссылается выпадающий список
sheet['A1'] = 'Новое значение'

# Пересчет формул в книге
workbook.calculation

# Сохранение изменений
workbook.save('example.xlsx')
