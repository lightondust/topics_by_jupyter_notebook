def iter_n_items(iterator, n):
    """
    :param iterator: iterator, for list use iterator = iter(lst); res = iter_n_items(iterator)
    :param n:
    :return:
    """
    res = []
    count = 0
    for i in iterator:
        count += 1
        if count > n:
            break
        res.append(i)
    return res
