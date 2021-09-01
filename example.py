from Base_num import Base_num

print(Base_num.decimal_to_basenum(255, Base_num.BIN).base_number)
print(Base_num.decimal_to_basenum(255,Base_num.HEX).base_number)

print((Base_num.decimal_to_basenum(10,Base_num.HEX)+Base_num.decimal_to_basenum(5,Base_num.HEX)).base_number)