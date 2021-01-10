
def removeAbnormalSpaces(x: str) -> str:
    """
    Remove abnormal spaces:
    1. double spaces "  "
    2. text start with space
    3. text end with space
    """
    while "  " in x:
        x = x.replace("  ", " ")
    while len(x) > 0 and x[0] == " ":
        x = x[1:]
    while len(x) > 0 and x[-1] == " ":
        x = x[:-1]
    return x


def selectTextBetween(x: str, left: str, right: str) -> list:
    """
    Select all text between left string and right string.
    """
    if not left in x:
        return []
    result = []
    li = x.split(left)
    for i in range(1, len(li)):
        if right in li[i]:
            result.append(li[i].split(right)[0])
    return result


def checkStartChars(text: str, chars: str) -> bool:
    """
    Check the starting charaters is equel to chars.
    """
    x, y = len(text), len(chars)
    if x < y:
        return False
    if text[:y] == chars:
        return True
    return False
