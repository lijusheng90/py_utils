def list_split(this_list, this_size):
    index_pre = 0
    for i, member_id in enumerate(this_list, 1):
        if i - index_pre == this_size:
            yield this_list[index_pre:i]
            index_pre = i
    if index_pre != len(this_list):
        yield this_list[index_pre:]


def test_list_split():
    qr_str_list = [i for i in range(10)]
    assert list(list_split(qr_str_list, -1)) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert list(list_split(qr_str_list, 0)) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert list(list_split(qr_str_list, 1)) == [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    assert list(list_split(qr_str_list, 3)) == [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    assert list(list_split(qr_str_list, 4)) == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]
    assert list(list_split(qr_str_list, 5)) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    assert list(list_split(qr_str_list, 10)) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    assert list(list_split(qr_str_list, 11)) == [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]


if __name__ == "__main__":
    test_list_split()
