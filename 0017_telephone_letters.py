import itertools


class Solution(object):
    def get_letters_list(self, digits):
        letters_list = []
        for x in digits:
            if x == "2":
                letters_list.append(["a", "b", "c"])
            elif x == "3":
                letters_list.append(["d", "e", "f"])
            elif x == "4":
                letters_list.append(["g", "h", "i"])
            elif x == "5":
                letters_list.append(["j", "k", "l"])
            elif x == "6":
                letters_list.append(["m", "n", "o"])
            elif x == "7":
                letters_list.append(["p", "q", "r", "s"])
            elif x == "8":
                letters_list.append(["t", "u", "v"])
            elif x == "9":
                letters_list.append(["w", "x", "y", "z"])
        return letters_list

    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        letters_list = self.get_letters_list(digits)
        return list(''.join(pair) for pair in itertools.product(*letters_list))


sol = Solution()
print(sol.letter_combinations(""))
