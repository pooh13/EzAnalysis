import jieba_hant
from collections import Counter
import stopWords

def MyJieba_hant(context):
    # print("原文內容："+context)
    sentence=([word for word in jieba_hant.cut(context, cut_all=False) if word not in stopWords.stopWords()[0] and word not in stopWords.stopWords()[1]])
    # print("斷詞結果：",sentence)
    # -------------------------------------------------------------------------
    cnt = Counter()

    for x in sentence:
        if len(x)>1 and x != '\r\n':
            cnt[x] += 1

    # print("字詞出現頻率統計結果\n")
    for (k,v) in cnt.most_common(5):
        # print("%s%s %s  %d" % ("  "*(5-len(k)), k, "*"*int(v/3), v))
        result = k+","+str(v)
        # print(result)
        return result

    print("\n"+"-"*80+"\n")
