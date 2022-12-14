import re

five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'


five_reg_exp=r'\d{5}'

print("-----------------------------------")

print(re.search(five_reg_exp,five_digit_zip))
print(re.search(five_reg_exp,nine_digit_zip))
print(re.search(five_reg_exp,phone_number))

print("-----------------------------------")
