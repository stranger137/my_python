def parity(a):
    if floor(a) == a: #�������� �� ������� �����
        if a mod 2 == 0:
            return "It is even"
        else:
            return "It is odd"
    else:
        return "The number is not integer"
        