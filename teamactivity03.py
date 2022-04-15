import math

class Fraction:
#initiat Fraction with numerator 0 and denominator 1
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        self.denominator = denominator
#display 0/1    
    def display(self):
        print(f'{self.numerator}/{self.denominator}')    
#prompt user for numerator
#prompt user for denominator
    def prompt(self):
        self.numerator = int(input('Enter the numerator:' ))
        self.denominator = int(input('Enter the denominator:' ))
#find if given fraction is improper
#find the whole number
#find the new numerator
#display the whole or mixed number        
    def display_decimal(self):
        if self.numerator > self.denominator:
            whole_number = self.numerator // self.denominator
            numerator = (self.numerator % self.denominator)
            denominator = self.denominator
            if numerator == 0:
                print(f'{whole_number}')
            else:
                print(f'{whole_number} {numerator}/{denominator}')
                print(f'{self.numerator/self.denominator}')
        else:
            print(f'{self.numerator}/{self.denominator}')
            print(f'{self.numerator/self.denominator}')
#check if there is a whole number
#if there is a whole number print the mixed number
#or find the common denominator
#reduce fraction
    def reduce(self):
        whole_number = self.numerator // self.denominator
        numerator = (self.numerator % self.denominator)
        denominator = self.denominator
        if whole_number >= 1:
            print('The reduced fraction is:')
            print(f'{whole_number} {numerator}/{denominator}')
        else:
            common_den = math.gcd(self.numerator, self.denominator)
            reduced_numerator = int(self.numerator/common_den)
            reduced_denominator = int(self.denominator/common_den)
            print('The reduced fraction is:')
            print(f'{reduced_numerator}/{reduced_denominator}')
#prompt for a second numerator
#prompt for a second denominator
#multiply original fraction with second fraction
    def multiply_by(self):
        numerator = int(input('Enter a second numerator: '))
        denominator = int(input('Enter a second denominator: '))
        mult_num = self.numerator * numerator
        mult_den = self.denominator * denominator
#Check if fraction is improper and print the whole or mixed number
        if mult_num > mult_den:
            whole_number = mult_num // mult_den
            new_numerator = (mult_num % mult_den)
            new_denominator = mult_den
            if new_numerator == 0:
                print(f'{whole_number}')
            else:
                print(f'{whole_number} {new_numerator}/{new_denominator}')
                print(f'{mult_num/mult_den}')
#if the value is a proper fraction print fraction
        else:
            print(f'{mult_num}/{mult_den}')
            print(f'{mult_num/mult_den}')
#check for a whole number and print the mixed number
#if value can be reduced print reduced fraction
        whole_number = mult_num // mult_den
        new_numerator = (mult_num % mult_den)
        new_denominator = mult_den
        if whole_number >= 1:
            print()
            print('The reduced fraction is:')
            print(f'{whole_number} {new_numerator}/{new_denominator}')
        else:
            common_den = math.gcd(mult_num, mult_den)
            reduced_numerator = int(mult_num/common_den)
            reduced_denominator = int(mult_den/common_den)
            print()
            print('The reduced fraction is:')
            print(f'{reduced_numerator}/{reduced_denominator}')        
                
def main():
    rat_num = Fraction()
    print()
    rat_num.display()
    rat_num.prompt()
    rat_num.display_decimal()
    print()
    rat_num.reduce()
    print()
    rat_num.multiply_by()
    
    
# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()