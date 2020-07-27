def compare_version(version1, version2):
    """
    :param version1: like x1.x2.x3.xn  xn is int
    :param version2:
    :return: 1 when version1 > version2;  0 when version1 == version2; -1 when version1 < version2 or error
    """
    try:
        l1 = version1.split('.')
        l2 = version2.split('.')
        for i in range(max(len(l1), len(l2))):
            if i >= len(l1) and int(l2[i]) != 0:
                return -1
            elif i >= len(l2) and int(l1[i]) != 0:
                return 1
            if i < len(l1) and i < len(l2):
                if int(l1[i]) > int(l2[i]):
                    return 1
                elif int(l2[i]) > int(l1[i]):
                    return -1
        return 0
    except ValueError:
        return -1


if __name__ == "__main__":
    print(compare_version("1.2.3", "1.0.0"))
