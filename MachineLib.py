#Negative = -1, zero = 0, positive = 1
def sign(num):
    if num > 0:
       sign = 1
    elif num < 0:
       sign = -1
    else:
       sign = 0
    return sign

#Converts a fraction to a decimal.
def frac_to_dec(numerator, denominator):
    decimal = float(numerator) / float(denominator)
    return decimal

#Rounds num to (figures) significant figures.
def round_xsf(num, figures):
    
    if '/' in str(num): #Fraction
      frac_list = str(num).split('/') 
      num = frac_to_dec(frac_list[0], frac_list[1])
    
    elif '**' in str(num): #Indices
       Indices_list = str(num).split('**')
       length_i = len(Indices_list)
       total = float(Indices_list[0]) ** float(Indices_list[1])
       count = 2
       while count < length_i:
          total = total ** float(Indices_list[count])
          count = count + 1
      
       num = total 
       
    elif '*' in str(num): #Multiplication
      multiplication_list = str(num).split('*')
      length_m = len(multiplication_list)
      total = float(multiplication_list[0]) * float(multiplication_list[1])
      count = 2
      while count < length_m:
         total = total * float(multiplication_list[count])
         count = count + 1

      num = total

    elif '+' in str(num): #Addition
      addition_list = str(num).split('+')
      len_a = len(addition_list)
      total = float(addition_list[0])
      count = 1
      while count < len_a:
         total = total + float(addition_list[count])
         count = count + 1
      
      num = total
   
    elif '- ' in str(num): #Subtraction
      subtraction_list = str(num).split('-')
      length_s = len(subtraction_list)
      total = float(subtraction_list[0])
      count = 1
      while count < length_s:
         total = total - float(subtraction_list[count])
         count = count + 1
      
      num = total
    
    else:
      pass

    num = float(num)
    figures = int(figures)
    
    if (num) - int(num) == 0: #Integer
       if sign(num) == -1: #Negative Integer
          decimalPlaces = figures + 1 - len(str(int(num)))
       
       else: #Zero or Positive Integer
          decimalPlaces = figures - len(str(int(num)))
          
       rounded = round(num, decimalPlaces)
       
    elif int(num) > 0: #Float, > 1
       len_b4_dp = len(str(int(num)))
       len_aft_dp = len(str(num)) - len_b4_dp 
       decimalPlaces= figures + len_aft_dp - len(str(num))
       rounded = round(num, decimalPlaces)
       
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
          rounded = round(hold1, decimalPlaces)
     
       else: #Float, abs < 1
          decimalPlaces = figures - 1 + count 
          rounded = round(hold1, decimalPlaces)    

    return rounded

def factorial(input):
    input = int(input)
    total = input
    for i in range (2, input):
        total = total * i 
    return total

def nCr(n, r):
    return (factorial(n)) / (factorial(int(n) - int(r)) * factorial(r))

#Let X be the discrete random variable 'number of times event occurs.'
# X ~ B(n, p), where n is the number of trials, and p is the probability of an event occuring during a trial.
def bin_P(tail, r, n, p):
    r = int(r)
    n = int(n)
    p = float(p)

    if tail == 'L': #P(X <= r)
       total_probability = (1 - p) ** n 
       for r in range (1, (r + 1)): #Sum of probabilities up to and including r
           total_probability = total_probability + (nCr(n, r) * (p ** r) * (1 - p) ** (n - r))
        
       return round_xsf(total_probability, 4)

    elif tail == 'M': #P(X = r)
       if r > 0: #P(X = r), r > 0
          return round_xsf((nCr(n, r) * (p ** r) * (1 - p) ** (n - r)), 4)
       
       else: #P(X = 0)
          return round_xsf(((1 - p) ** n), 4)

    else: #P(X >= r)
       if r > 0: #P(X >= r), r > 0
          return round_xsf((1 - bin_P('L', (r - 1), n, p)), 4)
       
       else: #P(X >= 0)
          return 1

#Searches for a keyword in a list of strings, and returns a list of indices referring to the strings the keyword is in.
def word_search(list_strings, keyword, exceptions):
    indices = []
    for i, string in enumerate(list_strings):
        words = string.split()
        testing_words = [word.rstrip(''.join(exceptions)).lower() for word in words]
        if keyword.lower() in testing_words:
           indices.append(i)
    
    return indices

#Searches for multiple keywords in a list of strings, and creates a dictionary of keywords to indices.
def multi_word_search(list_strings, keywords, exceptions):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(list_strings, keyword, exceptions)

    return keyword_to_indices

#Counts the number of words in a string.
def word_count(text):
    text_list = str(text).split(' ')
    for i in range(len(text_list) + 1):
        try:
          text_list.remove('')
        
        except Exception:
          pass

    return len(text_list)