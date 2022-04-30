def count_chars(data: str):
    data = data.lower()
    res = []
    for i in range(97, 123):
        tmp = data.count(chr(i))
        res.append(tmp)
    return res

