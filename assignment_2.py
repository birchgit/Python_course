def translate_numeral(number):    if type(number) == str:  # check type of input        roman_numeral = number        #======enter code below======                c_map= {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100,'D' : 50, 'M' : 1000}        arabic_number = 0        for i in range(len(roman_numeral)):                        if  i > 0 and c_map[roman_numeral[i-1]] < c_map[roman_numeral[i]]:                 arabic_number +=  c_map[roman_numeral[i]] - 2 * c_map[roman_numeral[i-1]]                             else:                  arabic_number += c_map[roman_numeral[i]]                         # ======enter code above======        print('{0} translated to {1}!'.format(roman_numeral, arabic_number))  # print the result        return arabic_number    else:        print('Input not valid.')if __name__ == '__main__':    input_numerals = ['X', 'XXVIII', 'LXXI', 'XCIX', 'MCMXCIV']    outputs = [10, 28, 71, 99, 1994]    results = [True, True, True, True, True]    for index in range(5):        if translate_numeral(input_numerals[index]) != outputs[index]:            results[index] = False    if False in results:        print('Not all numerals translated correctly. Try again.')    else:        print('Well done! All numerals translated correctly.')