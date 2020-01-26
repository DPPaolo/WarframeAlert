def divide_for_n(message, num, divide="\n"):
    if (divide == ""):
        return None
    data = []
    for i in range(0, num):
        data.append("")
    i = 0
    message = message.split(divide)
    for elem in message:
        data[i % num] = data[i % num] + elem + divide
        i += 1
    data[-1] = data[-1][:-1]
    return data


def set_barred(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])
