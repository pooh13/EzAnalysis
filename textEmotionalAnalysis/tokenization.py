import JiebaResult

def tokenization(tableQueryList, textQueryList):
    bow = set()
    comment_bow = dict()
    context = JiebaResult.JiebaResult(textQueryList)

    for i in range(len(tableQueryList)):
        comment_bow.update({i: set(context)})
        bow = bow.union(set(context))
        # print(bow)

    return comment_bow, bow
