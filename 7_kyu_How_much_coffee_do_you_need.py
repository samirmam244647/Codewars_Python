def how_much_coffee(events):
    c = 0
    for i in events:
        if i in ["cw","dog","cat","movie"]:
            c += 1
        elif i in ["CW","DOG","CAT","MOVIE"]:
            c += 2
    return (c if c <4 else 'You need extra sleep')

#https://www.codewars.com/kata/57de78848a8b8df8f10005b1