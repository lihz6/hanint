#!/usr/bin/env python3
from functools import reduce

_unit = reduce(
    lambda xs, u: [*[x + u for x in xs], *xs],
    ['万', '亿', '兆'], ['千', '百', '十', '']
)

_base = '零一二三四五六七八九'
_full = '０１２３４５６７８９'
_half = '0123456789'


def _step_1(nstr):

    delta = len(_unit) - len(nstr)
    if delta < 0:
        raise Exception('out of range')
    return [_base[int(i)] + u for i, u in zip(nstr, _unit[delta:])]


def _step_2(nums):
    def func1(arr, num):
        last = arr[-1][-1]
        if last == num[-1]:
            arr[-1] += num
            return arr
        pop = _step_2(arr.pop()[:-1].split(last))
        arr.append(pop + last if pop else '零')
        arr.append(num)
        return arr

    def func2(s, n): return s if s[-1] == n else s + n

    return reduce(func2, reduce(func1, nums[1:], nums[:1])).rstrip('零')


def _encode(num):
    text = _step_2(_step_1(str(num)))
    if text.startswith('一十'):
        return text[1:]
    return text


# export API:
def encode(num):
    try:
        num = int(num)
    except:
        num = decode(num)
    if num < 0:
        return '负' + _encode(-num)
    if num > 0:
        return _encode(num)
    return '零'


def _decode(han):
    num = 0
    for u, p in ('兆', 16), ('亿', 8), ('万', 4), ('千', 3), ('百', 2), ('十', 1):
        if u not in han:
            continue
        i = han.index(u)
        num += _decode(han[:i] or '一')*10**p
        han = han[i+1:]
    for u, p in zip(han, range(len(han)-1, -1, -1)):
        num += _base.index(u)*10**p
    return num


def decode(han):
    han = str(han).replace('两', '二')
    for h, f, b in zip(_half, _full, _base):
        han = han.replace(h, b).replace(f, b)
    try:
        if han.startswith('负'):
            return -_decode(han[1:])
        return _decode(han)
    except:
        return int(han)


def full2half(text):
    if type(text) is not str:
        return text
    for f, h in zip(_full, _half):
        text = text.replace(f, h)
    return text


def main():
    import sys
    for arg in sys.argv[1:]:
        try:
            print('[E]', encode(int(arg)))
        except:
            try:
                print('[D]', decode(arg))
            except:
                pass


if __name__ == '__main__':
    main()
# 算法描述：

# 1. 输入：4567890123
# 2. 数组：[4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
# 3. 转换：['四', '五', '六', '七', '八', '九', '零', '一', '二', '三']
# 3. 加入进位：['四十亿', '五亿', '六千万', '七百万', '八十万', '九万', '零千', '一百', '二十', '三']
# 4. 假设函数 read 能将 #3 的数组转化成最后的读法，
#    即是：read(['四十亿', '五亿', '六千万', '七百万', '八十万', '九万', '零千', '一百', '二十', '三'])
#    递归：read(['四十', '五']) + '亿' + read(['六千', '七百', '八十', '九']) + '万' + read(['零']) + '千' + read(['一']) + '百' + read(['二']) + '十' + '三'
# 5. 通过层层递归：'四十五亿六千七百八十九万零一百三十三'


# 参考：

# 数的分级读法：https://wenku.baidu.com/view/73e3ec5f04a1b0717fd5ddb4.html
# 　　　　　　　https://wenku.baidu.com/view/495d9c4f2e3f5727a5e9626a.html
# 自乘进位系统：https://zhidao.baidu.com/question/467103224.html
