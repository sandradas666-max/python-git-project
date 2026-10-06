rice_price=45
rice_quantity=3

sugar_price=40
sugar_quantity=2.5

oil_price=130
oil_quantity=1.8

total_cost_rice=rice_price * rice_quantity
total_cost_sugar=sugar_price * sugar_quantity
total_cost_oil=oil_price * oil_quantity

print(total_cost_rice)
print(total_cost_sugar)
print(total_cost_oil)

final_total_bill=(total_cost_rice + total_cost_sugar + total_cost_oil)
print("final_total_bill is",final_total_bill)

convert_int=int(final_total_bill)
print("convert to integer",convert_int)

convert_str=str(final_total_bill)
print("convert to string",convert_str)

print(type(convert_str))

convert_float=float(convert_str)
print("print data type of final_total_bill",type(convert_float))

import random
delivery_charge=(random.randint(5, 10))
print("random number is",delivery_charge)

total_charge=(final_total_bill + delivery_charge)
print("total_charge is",total_charge)
