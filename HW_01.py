# 1. Напишите программу, удаляющую из текста все слова, 
#    содержащие "абв". В тексте используется 
#    разделитель пробел.

# in Number of words: 10
# out авб абв бав абв вба бав вба абв абв абв
#     авб бав вба бав вба

# in Number of words: 6
# out ваб вба абв ваб бва абв
#     ваб вба ваб бвa


from random import sample

def list_elem(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        letters = sample(alp, 3)
        words_list.append("".join(letters))
    return " ".join(words_list)


#def list_rand_words(count: int, alp: str = 'абв'):
#     return " ".join("".join(sample(alp, 3)) for _ in range(count))

def del_elem(words: str) -> str:
    return " ".join(words.replace("абв", "").split())    

my_list = list_elem(int(input("Введите: ")))
print(my_list) 
print(del_elem(my_list))