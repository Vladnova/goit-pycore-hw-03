from typing import List
import random

def get_numbers_ticket(min:int, max:int, quantity:int)->List[int]:
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return []
    
    lottery_numbers = random.sample(range(min, max), quantity)
    return sorted(lottery_numbers)  

print(get_numbers_ticket(min = 1, max = 25, quantity=5))
print(get_numbers_ticket(min = -5, max = 55, quantity=1))
