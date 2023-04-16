class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = None
        last_char_was_negative = False
        last_char_was_digit = False
        final_negative = False
        for x in s.lstrip():
            if x == '-':
                last_char_was_negative = True
                last_char_was_digit = True
            if x.isdigit():
                if result is None:
                    result = int(x)
                else:
                    result = int(str(result) + x)
                if last_char_was_negative and last_char_was_digit:
                    final_negative = True
                    last_char_was_negative = False
                last_char_was_digit = True
            elif not x.isdigit() and last_char_was_digit:
                if last_char_was_negative and x != '-':
                    last_char_was_negative = False
                elif last_char_was_negative and x == '-':
                    continue
                else:
                    break
        if final_negative:
            return -result
        else:
            return result


sample = "-w-0rds and 987"
var = Solution()
print(var.myAtoi(sample))
