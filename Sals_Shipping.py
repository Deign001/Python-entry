#!/bin/python3

print("Sals Shipping")
weight = 4.8

#Ground Shipping
if weight <= 2:
  cost_ground = 1.50 * weight + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = 3.00 * weight + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = 4.00 * weight + 20.00
elif weight > 10:
  cost_ground = 4.75 * weight + 20.00
print("Ground Shipping $", cost_ground)
#Premium Shipping
Premium_Ground_Shipping = 125.00
print("Premium Ground Shipping $",Premium_Ground_Shipping)

#Drone Shipping

if weight <= 2:
  drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12.00
elif weight > 10:
  drone_cost = weight * 14.25
print("Drone Shipping $", drone_cost)



