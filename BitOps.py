import sys


class BitOps:

    def __innit__(self):
        ''''''


    def check_LSB(self, num):

        if num & 1:

            return 1

        else:

            return 0


    def check_MSB(self, num):

        bits = sys.getsizeof(num) * 8
        msb = 1 << (bits - 1)

        if num & msb:

            return 1

        else:

            return 0


    def check_nth_bit(self, num, nth_bit):

        bits = sys.getsizeof(num) * 8
        sb = nth_bit << (nth_bit - 1)

        if nth_bit > bits:
            return "Invalid input"

        if num & sb:

            return 1

        else:

            return 0


    def set_nth_bit(self, num, nth_bit):

        bits = sys.getsizeof(num) * 8

        if nth_bit > bits:
            return "Invalid input"

        set_bit = 1 << (nth_bit - 1) | num

        return set_bit


    def clear_nth_bit(self, num, nth_bit):

        bits = sys.getsizeof(num) * 8

        if nth_bit > bits:
            return "Invalid input"

        clear_bit = ~(1 << (nth_bit - 1)) & num

        return clear_bit


    def swap(self, num1, num2):

        num1 ^= num2
        num2 ^= num1
        num1 ^= num2

        return num1, num2

