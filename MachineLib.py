def sign(num):
    if num > 0:
       sign = 1
    elif num < 0:
       sign = -1
    else:
       sign = 0
    return sign

def frac_to_dec(numerator,denominator):
    decimal = float(numerator) / float(denominator)
    return decimal

def round_xsf(num,figures):
    
    if ',' in str(num): #Fraction
      frac_list = str(num).split(',') 
      num = frac_to_dec(frac_list[0],frac_list[1])
    
    else:
      pass

    num=float(num)
    
    if (num) - int(num) == 0: #Integer
       if sign(num) == -1: #Negative Integer
          decimalPlaces = figures + 1 - len(str(int(num)))
       
       else: #Zero or Positive Integer
          decimalPlaces = figures - len(str(int(num)))
          
       rounded = round(num,decimalPlaces)
       
    elif int(num) > 0: #Float, > 1
       len_b4_dp = len(str(int(num)))
       len_aft_dp = len(str(num))-len_b4_dp - 1
       decimalPlaces= figures + 1 + len_aft_dp - len(str(num))
       rounded = round(num,decimalPlaces)
       
    else: #Negative Float or Float, < 1
       hold1 = num 
       hold2 = abs(num)
       num = abs(num)
       count = 0
       while num < 1:
             count = count + 1
             num = 10 * num    
       
       if sign(hold1) == -1 and hold2 > 1: #Negative Float, abs > 1
          len_b4_dp = len(str(int(num)))
          len_aft_dp = len(str(num)) - len_b4_dp - 1
          decimalPlaces = figures + 1 + len_aft_dp - len(str(num))
          rounded = round(hold1,decimalPlaces)
     
       else: #Float, abs < 1
          decimalPlaces = figures - 1 + count 
          rounded = round(hold1,decimalPlaces)    

    return rounded


    