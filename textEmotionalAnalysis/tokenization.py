import JiebaResult

def tokenization(queryList):

    bow = set()
    comment_bow = dict()
    context = JiebaResult.JiebaResult(queryList)

    # ----- len()
    # for i in range(len(tableQueryList)):
    #     comment_bow.update({i: set(context)})
    #     bow = bow.union(set(context))
    #     # print(bow)

    # ----- enumerate()
    for (k,v) in enumerate(context, 0):
        comment_bow.update({k: set(v)})
        bow = bow.union(set(v))

    return comment_bow, bow
