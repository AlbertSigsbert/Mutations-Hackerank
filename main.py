def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string


def mutate_string_alt(string, position, character):
    string = string[:position] + character + string[(position + 1):]
    return string


s = input()
i, c = input().split()

mutatedString = mutate_string_alt(s, int(i), c)
print(mutatedString)
