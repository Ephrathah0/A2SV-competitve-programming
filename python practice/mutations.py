def mutate_string(string, position, character):
    new_istl = list(string)
    new_istl[position] = character
    string = ''.join(new_istl)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
