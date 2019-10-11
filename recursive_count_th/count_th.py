'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    letters = 'th'
    test = word[0:2]
    
    if len(test) != 2:
        return 0
    elif letters == test:
        return 1 + (count_th(word[1:]))
    else:
        return count_th(word[1:])