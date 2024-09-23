calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]

info_1 = string_info("Hello World")
info_2 = string_info("PythoN")

contains_1 = is_contains("hello", ["hello", "world", "python"])
contains_2 = is_contains("JAVA", ["Java", "C++", "PHP"])

print("Информация о строке 1:", info_1)
print("Информация о строке 2:", info_2)
print("Содержит 'hello':", contains_1)
print("Содержит 'JAVA':", contains_2)

print("Общее количество вызовов функций:", calls)