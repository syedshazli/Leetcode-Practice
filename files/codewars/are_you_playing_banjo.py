def are_you_playing_banjo(name):
    # IPython character/string methods
    newname = name[0]
    if newname == 'r' or newname == 'R':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
