from importlib.resources import contents

filename = 'text_file.txt'

text = """Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом."""

with open(filename, "w", encoding='utf-8') as file:
    file.write(text)

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)