import itertools


class Solution(object):
    def get_letters_list(self, digits):
        corresponding_telephone_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        letters_list = [corresponding_telephone_letters[x] for x in digits if x in corresponding_telephone_letters]
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
print(sol.letter_combinations("23"))
