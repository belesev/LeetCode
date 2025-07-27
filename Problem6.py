class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = []
        full_cycle = (numRows - 2) * 2 + 2

        # first row
        for i in range(len(s)):
            if i % full_cycle == 0:
                res.append(s[i])
        print("".join(res))

        # other rows where there are 2 symbols:
        for shift in range(1, numRows-2 + 1):
            for i in range(len(s)):
                if i % full_cycle in (shift, full_cycle-shift):
                    res.append(s[i])
        print("".join(res))

        # last row
        for i in range(len(s)):
            if i % full_cycle == numRows-1:
                res.append(s[i])
        print("".join(res))

        return "".join(res)


def test_problem6():
    s = Solution()
    assert s.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert s.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert s.convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN"
    assert s.convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"
    assert s.convert("A", 1) == "A"


if __name__ == "__main__":
    test_problem6()