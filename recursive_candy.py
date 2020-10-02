import math


#compute recursive wrappers
def rec_wrappers(wrap_cost, candies):
   print("You eat ", candies," candies.")
   wrappers = candies - (candies % 3)
   if(wrappers/wrap_cost < 1):
      return 0;
   candies = wrappers/wrap_cost
   print("You trade your wrappers for ", candies," more candies.")
   return candies + rec_wrappers(wrap_cost, candies);

# compute candies from money
def max_candies(money, cost, wrap_cost):
   candies = int(money/cost)
   print("You trade your money for ", candies, " candies.")
   print("You begin to eat candies and trade the wrappers for more.")
   return candies + rec_wrappers(wrap_cost, candies);

# driver code
cost = 0.25
print("Each candy costs $", cost)
money = float(input("How much money would you like to spend? $"))
money = money - (money % cost)

wrap_cost = int(3) #number of wrappers needed to trade for a candy

total_candies = max_candies(money, cost, wrap_cost)
print("In total, you ate ", total_candies," candies! ¡Que ganga!")