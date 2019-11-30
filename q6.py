tup = [('Tom', 19, 80), ('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85)]


def by_name(t):
    return t[0]


def by_age(t):
    return t[1]


def by_score(t):
    return t[2]


tup = sorted(tup, key=by_score)
tup = sorted(tup, key=by_age)
tup = sorted(tup, key=by_name)

print(tup)

