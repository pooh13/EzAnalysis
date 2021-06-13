import cursorToPd

def twoTypeClassify(queryList, resetColumn, newColumn):

    df = cursorToPd.cursorToPd(queryList, 2)

    new_df = df[df[resetColumn]!=3].reset_index(drop=True)

    for i in range(len(new_df)):
        if(int(new_df.loc[i, resetColumn]) < 3):
            new_df.loc[i, newColumn] = 0
        else:
            new_df.loc[i, newColumn] = 1

    new_df[newColumn] = new_df[newColumn].astype(int)

    result = new_df[newColumn]

    return result
