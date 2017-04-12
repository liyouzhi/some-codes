# -*- coding:utf-8 -*-
import sys

def income_calc(before_tax):
    tax_income = before_tax - 3500
    if tax_income <= 0:
        ratio = 0
        deduct = 0
    elif tax_income <= 1500:
        ratio = 0.03
        deduct = 0
    elif tax_income <= 4500:
        ratio = 0.1
        deduct = 105
    elif tax_income <= 9000:
        ratio = 0.2
        deduct = 555
    elif tax_income <= 35000:
        ratio = 0.25
        deduct = 1005
    elif tax_income <= 55000:
        ratio = 0.3
        deduct = 2755
    elif tax_income <= 80000:
        ratio = 0.35
        deduct = 5505
    else:
        ratio = 0.45
        deduct = 13505

    insurance_base_down = 2834    
    insurance_base_up = 21258
    if before_tax <= insurance_base_down:
        base = insurance_base_down
    elif before_tax >= insurance_base_up:
        base = insurance_base_up
    else:
        base = before_tax
    
    insurance = base * 0.122 + 3
    gongjijin = base * 0.12 

    tax = (tax_income - gongjijin - insurance) * ratio -deduct
    income = before_tax - tax - gongjijin - insurance

    print('税后:%.2f  保险:%.2f  公积金:%.2f  税:%.2f' % (income, insurance, gongjijin, tax))

# income_calc(28000)

if __name__ == '__main__':
    wage = int(sys.argv[1])
    income_calc(wage)
    
