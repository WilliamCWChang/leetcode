from typing import List


def test_leetcode1():
    assert Solution().reverse(123) == 321
    assert Solution2().reverse(123) == 321


def test_leetcode2():
    assert Solution().reverse(-123) == -321
    assert Solution2().reverse(-123) == -321


def test_leetcode3():
    assert Solution().reverse(120) == 21
    assert Solution2().reverse(120) == 21


def test_leetcode4():
    assert Solution().reverse(1534236469) == 0
    assert Solution2().reverse(1534236469) == 0


class Solution2:
    def reverse(self, x: int) -> int:
        def sign(x):
            return x and (1, -1)[x < 0]
        r = int(str(sign(x)*x)[::-1])
        return (sign(x)*r, 0)[r > 2**31 - 1]


class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        if x[0] == '-':
            x.pop(0)
            y = True
        else:
            y = False
        x.reverse()
        # print(x)
        x = int("".join(x))
        if y:
            x = x * -1
        if abs(x) <= 2147483648:
            return x
        else:
            return 0
