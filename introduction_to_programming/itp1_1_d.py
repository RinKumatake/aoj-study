def watch(s:int) -> int:
    """秒数sが与えられるのでhh:mm:ssの書式に変換する
    :param s: 変換する秒数
    :return: hh:mm:ssの書式に変換した時間
    """
    hour = s // 3600
    x = s % 3600
    minute = x // 60
    second = x % 60
    return "{}:{}:{}".format(hour, minute, second)

s = int(input())
print(watch(s))