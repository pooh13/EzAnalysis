import jieba_hant
from collections import Counter
import stopWords

def MyJieba_hant(context):

    # print("原文內容："+context)
    sentence = ([word for word in jieba_hant.cut(context, cut_all=False) if word not in stopWords.stopWords()[0]])
    # print("斷詞結果：",sentence)

    return sentence

    # ----- limit(5)
    # cnt = Counter()
    #
    # for x in sentence:
    #     if len(x)>1 and x != '\r\n':
    #         cnt[x] += 1
    # # print("字詞出現頻率統計結果\n")
    #
    # return[k for (k,v) in cnt.most_common(5)]

