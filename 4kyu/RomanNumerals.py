from itertools import chain, tee, zip_longest
class RomanNumerals:
    ROMAN_NUMS={   
                "M" : 1000,  
                "CM": 900, 
                "D" : 500,
                "CD": 400,
                "C" : 100,
                "XC": 90,
                "L" : 50,
                "XL": 40,
                "X" : 10,
                "IX": 9, 
                "V" : 5,
                "IV": 4,
                "I" : 1
                 }
    NUMS_ROMAN={
                number : roman_symbol
                for roman_symbol, number in ROMAN_NUMS.items()
                    }
     
    def to_roman(val : int) -> str:
        roman_string=""
        for el in RomanNumerals.NUMS_ROMAN:
            while val - el >= 0:
                    roman_string+=RomanNumerals.NUMS_ROMAN[el]
                    val -= el
        return roman_string
    
#i thought this one was easier and implemented it first, then figured out: 
#i can use to_roman to loop through the valid input and find the correct output :) dont know about performance of that though, will test
        
    @staticmethod
    def from_roman(roman_num : str) -> int:  
        outp = 0
        roman_chain = chain(roman_num)
        curr_iter, next_iter = tee(roman_chain,2)
        next(next_iter, None)
        
        for el, next_el in zip_longest(curr_iter, next_iter):
            print(el, next_el)
            if next_el is not None:
                if RomanNumerals.ROMAN_NUMS[el]<RomanNumerals.ROMAN_NUMS[next_el]:
                    outp+=RomanNumerals.ROMAN_NUMS[next_el]-RomanNumerals.ROMAN_NUMS[el]
                    next(curr_iter, None)
                    next(next_iter, None)
                    
                else: outp+=RomanNumerals.ROMAN_NUMS[el]
                print(outp)
            if next_el == None:
                outp+=RomanNumerals.ROMAN_NUMS[el]            
        return outp


test="MMCMXXIX"
print(RomanNumerals.from_roman(test))
print(RomanNumerals.to_roman(RomanNumerals.from_roman(test)))               
                
            
        
        