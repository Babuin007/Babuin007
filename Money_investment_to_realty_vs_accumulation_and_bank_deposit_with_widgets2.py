import matplotlib.pyplot as plt
from ipywidgets import widgets, interact, interactive, fixed, interact_manual
from IPython.core.display import display



def realty_investment(realty_cost = 8000000,
                      start_money=2000000,
                      credit_percent = 7.3,
                      deposit_percent = 5,
                      credit_years = 5,
                      percent_of_realty_cost_increase_per_year = 10,
                      realty_rent_per_month = 40000):
    credit_money = realty_cost - start_money
    months = credit_years * 12
    credit_percent_per_month = credit_percent / 100 / 12
    credit_pay_per_month = credit_money * (
                credit_percent_per_month + credit_percent_per_month /
                ((1 + credit_percent_per_month) ** months - 1))

    repair_and_furniture = realty_cost * 0.25
    repair_month = 6

    utilities_per_month = realty_cost * 0.0007

    expenses_per_month = [start_money]
    income_per_month = [0]
    expenses_per_month_with_income = [start_money]
    realty_cost_increase = [realty_cost]
    saved_money_no_percent = [start_money]
    saved_money_with_percent = [start_money]
    bank_percent_earned = [0]

    print ('Стоимость недвижимости -', realty_cost,'руб')
    print ('Начальная сумма -', start_money,'руб')
    print ('Сумма кредита -', credit_money,'руб')
    print ('Ежемесячный платеж банку -', round(credit_pay_per_month,0), 'руб')
    print ('Кредитный процент -', credit_percent,'%')
    print ('Банковский процент -', deposit_percent, '%')
    print ('Срок кредита -', credit_years,'лет')
    print ('Стоимость ремонт и мебели -', repair_and_furniture, 'руб')
    print ('Ежегодное увеличение стоимости недвижимости -', percent_of_realty_cost_increase_per_year, '%')
    print ('Сдача недвижимости в аренду -',realty_rent_per_month, 'руб')
    print()
    for month in range (months-1):
        if month < repair_month:
            current_expenses_per_month = expenses_per_month[-1] + repair_and_furniture/repair_month + credit_pay_per_month + utilities_per_month
            expenses_per_month.append (current_expenses_per_month)
            current_income_per_month = income_per_month[-1]
            income_per_month.append (current_income_per_month)
            realty_cost_increase_current = realty_cost_increase[-1]+ (percent_of_realty_cost_increase_per_year / 100 / 12) * realty_cost +repair_and_furniture/repair_month
            realty_cost_increase.append(realty_cost_increase_current)
            expenses_per_month_with_income.append(current_expenses_per_month-current_income_per_month)
            saved_money_with_percent.append(saved_money_with_percent[-1] + credit_pay_per_month + saved_money_with_percent[-1]*(deposit_percent/100/12))
            bank_percent_earned.append(bank_percent_earned[-1] + saved_money_with_percent[-1]*(deposit_percent/100/12))
            saved_money_no_percent.append( saved_money_no_percent[-1] + credit_pay_per_month)
        else:
            current_expenses_per_month = expenses_per_month[-1] + credit_pay_per_month
            expenses_per_month.append (current_expenses_per_month)
            current_income_per_month = income_per_month[-1] + utilities_per_month + realty_rent_per_month
            income_per_month.append (current_income_per_month)
            realty_cost_increase_current = realty_cost_increase[-1] + (percent_of_realty_cost_increase_per_year / 100 / 12) * realty_cost
            realty_cost_increase.append (realty_cost_increase_current)
            expenses_per_month_with_income.append (current_expenses_per_month - current_income_per_month)
            saved_money_with_percent.append (saved_money_with_percent[-1] + credit_pay_per_month + saved_money_with_percent[-1] * (deposit_percent / 100 / 12))
            bank_percent_earned.append (bank_percent_earned[-1] + saved_money_with_percent[-1] * (deposit_percent / 100 / 12))
            saved_money_no_percent.append (saved_money_no_percent[-1] + credit_pay_per_month)

    print ('Расходы (проценты банка + ст-ть ремонта + ст-ть КУ)-', round (credit_pay_per_month * months - credit_money + repair_and_furniture + utilities_per_month, 0),'руб')
    print ('Доходы за аренду -', round (income_per_month[-1], 0),'руб')
    print ('Расходы за вычетом доходов -', round (credit_pay_per_month * months - credit_money + repair_and_furniture + utilities_per_month - income_per_month[-1], 0),'руб')
    print ('Оплата кредита -', round (credit_pay_per_month * months, 0), 'руб')
    print ('Проценты банку -', round (credit_pay_per_month * months - credit_money, 0),'руб')
    print ('Накопление за период оплаты кредита (начальный капитал + кредит) -', round (credit_money + start_money, 0), 'руб')
    print ('Конечная стоимость недвижимости-', round (realty_cost_increase[-1], 0),'руб')
    print ('Накопление при инвестировании в недвижимость с учетом расходов -', round (realty_cost_increase[-1]-round(credit_pay_per_month * months - credit_money + repair_and_furniture + utilities_per_month - income_per_month[-1]), 0),'руб')
    print()
    print ('Накоплении с банковским процентом и начальным капиталом -',round (saved_money_with_percent[-1]+ credit_pay_per_month + saved_money_with_percent[-1] * (deposit_percent / 100 / 12), 0), 'руб')
    print ('Накоплении с банковским процентом без стартового капитала -',round (saved_money_with_percent[-1] + credit_pay_per_month + saved_money_with_percent[-1] * (deposit_percent / 100 / 12)- start_money, 0), 'руб')
    print ('Накоплении без банковского процента без стартового капитала -', round (saved_money_no_percent[-1] + credit_pay_per_month + saved_money_with_percent[-1] * (deposit_percent / 100 / 12)- start_money, 0), 'руб')
    print ('Процент при накоплении -', round (saved_money_with_percent[-1] - saved_money_no_percent[-1], 0), 'руб')

    plt.plot (range (months), realty_cost_increase)
#     plt.plot (range (months), expenses_per_month)
#     plt.plot (range (months), income_per_month)
    plt.plot (range (months), expenses_per_month_with_income)
    plt.plot (range (months), saved_money_with_percent)
#     plt.plot (range (months), bank_percent_earned)
#     plt.plot (range (months), saved_money_no_percent)

    plt.grid ()
    plt.xlabel ('Time, months')
    plt.ylabel ('Money, rub')
    plt.title ('Money investment to Realty')
    plt.legend (labels = ['realty_cost_increase',
#                           'expenses_per_month',
#                           'income_per_month',
                          'expenses_per_month_with_income',
                          'saved_money_with_percent',
#                           'bank_percent_earned',
#                           'saved_money_no_percent']
                         ])
    plt.show ()
realty_investment()

# interact(realty_investment,
#         realty_cost = widgets.IntSlider (min=3000000, max=15000000, step=500000, value=8000000),
#         start_money = widgets.IntSlider (min=1000000, max=10000000, step=500000, value=2000000),
#         credit_percent = widgets.FloatSlider (min=6, max=10, step=0.5, value=7.3),
#         deposit_percent = widgets.FloatSlider (min=6, max=10, step=0.5, value=5),
#         credit_years = widgets.IntSlider (min=1, max=30, step=1, value=5),
#         percent_of_realty_cost_increase_per_year = widgets.FloatSlider(min=6, max=100, step=0.5, value=10),
#         realty_rent_per_month = widgets.IntSlider (min=10000, max=100000, step=1000, value=40000))



