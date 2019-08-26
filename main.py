from BitOps import*

num = int(input("Enter an integer: "))
nth_bit = int(input("Enter bit of interest: "))
op = BitOps()
print(op.check_LSB(num))
print(op.check_MSB(num))
print(op.check_nth_bit(num, nth_bit))
print(op.set_nth_bit(num, nth_bit))
print(op.clear_nth_bit(num, nth_bit))
print(op.swap(20, 30))