def index_words(text):
    """
    Возвращает массив с индексами начала слов в тексте
    :param text:
    :return:
    """
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = 'some shitty text some'
result = index_words(address)
print(result)

#generator version of same function
def index_words2(text):
    """
    Возвращает массив с индексами начала слов в тексте
    :param text:
    :return:
    """
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1
