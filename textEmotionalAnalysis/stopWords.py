def stopWords():
    punctuation = set()
    with open('./textFunctions/punctuation_zh_tw.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            punctuation.add(line.strip())
    with open('./textFunctions/punctuation_en.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            punctuation.add(line.strip())
    punctuation.add('\n')
    punctuation.add(' ')

    with open('./textFunctions/stopwords_zh_tw.txt', encoding='utf-8') as file:  # 加入停用詞表
        stopwords = {line.strip() for line in file}

    return punctuation, stopwords
