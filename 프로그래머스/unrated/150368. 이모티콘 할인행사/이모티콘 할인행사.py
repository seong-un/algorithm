from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    
    sales = [0.9, 0.8, 0.7, 0.6]
    
    for sale in list(product(sales, repeat = len(emoticons))):
        plus = 0
        amount = 0
        for user in users:
            cost = 0
            for idx, ratio in enumerate(sale):
                if ratio <= 1 - user[0] / 100:
                    cost += emoticons[idx] * ratio
            
            if cost >= user[1]:
                plus += 1
            else:
                amount += cost
        
            if answer[0] < plus:
                answer = [plus, amount]
            elif answer[0] == plus:
                if answer[1] < amount:
                    answer = [plus, amount]
    
    return answer