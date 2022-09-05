def cost_calculator(*args, **keyword_args):
  topping = {
    "pepperoni" : 1,
    "mushroom"  : 0.50,
    "olive"     : 0.50,
    "anchovy"   : 2.00,
    "ham"       : 1.50
  }

  Drinks = {
    "small"  : 2.00,
    "medium" : 3.00,
    "large"  : 3.50,
    "tub"    : 3.75
  }

  Wings = {
    10 : 5.00,
    20 : 9.00,
    40 : 17.50,
    100 : 48.00
  }

  total_cost = 0
  discount = 0
  tax = 0

  for a in args:
    total_cost += 13
    for tops in a:
      total_cost += topping[tops]
  
  # print("pizza: ", total_cost)

  
  for k,v in keyword_args.items():
    if k=="drinks":
      for d in v:
        total_cost += Drinks[d]
    elif k=="wings":
      for w in v:
        total_cost += Wings[w]
    elif k=="coupon":
      discount = v

  #tax before discount
  # print("total before discount: ", total_cost)

  tax = total_cost*0.0625
  total_cost = total_cost*(1-discount) + tax
  total_cost = round(total_cost,2)
  # print("total after discount: ", total_cost)
  return total_cost      

# Execute this cell to grade your work
from bwsi_grader.python.pizza_shop import grader
grader(cost_calculator)
