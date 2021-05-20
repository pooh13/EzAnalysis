import JiebaResult

def tokenization(textQueryList):
    bow = set()
    comment_bow = dict()
    context = JiebaResult.JiebaResult(textQueryList)

    # print(context)
    # print(len(context))

    # ----- len()
    # for i in range(len(tableQueryList)):
    #     comment_bow.update({i: set(context)})
    #     bow = bow.union(set(context))
    #     # print(bow)

    # ----- enumerate()
    for (k,v) in enumerate(context, 0):
        comment_bow.update({k: set(v)})
        bow = bow.union(set(v))

    # print(comment_bow)
    # print(len(comment_bow))
    # print(bow)
    # print(len(bow))

    return comment_bow, bow
