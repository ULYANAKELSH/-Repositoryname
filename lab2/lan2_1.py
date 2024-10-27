money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
k=0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while (money_capital+salary-spend*(1+increase)**k>0):
    money_capital=money_capital-(spend*(1+increase)**k-salary)
    k+=1

print("Количество месяцев, которое можно протянуть без долгов:", k)
