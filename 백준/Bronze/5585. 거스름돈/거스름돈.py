A=int(input())
money=1000-A
coin=0

coin+=money//500
coin+=(money%500)//100
coin+=((money%500)%100)//50
coin+=(((money%500)%100)%50)//10
coin+=((((money%500)%100)%50)%10)//5
coin+=((((money%500)%100)%50)%10)%5

print(coin)