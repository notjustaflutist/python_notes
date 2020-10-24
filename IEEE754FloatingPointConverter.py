# convert decimal value with fractional part to IEEE754 Floating Point

# get value to convert
dec_value = input("Enter a base 10 value to convert: ")

# parse into sections
if "." in dec_value:
    dec_list = dec_value.split(".")
    dec_int = dec_list[0]
    dec_fract = dec_list[1]
else:
    dec_list = dec_value
    dec_int = dec_value
    dec_fract = 0

print(dec_value, dec_list, dec_int, dec_fract)

# convert dec_int to binary
bin_int = convert_base10_int_to_binary(dec_int)

# convert dec_fract to binary
bin_fract = convert_base10_fraction_to_binary(dec_fract)

# concatenate bin_int and bin_fract
bin_value = bin_int + bin_fract

# convert bin_value to scientific notation

# store the sign bit
# extract the normalized mantissa and pad to 23 bits
# add 127 to the exponent (bias the exponent)
# convert the exponent to binary
# concatenate the binary sign, biased exponent, normalized mantissa
# convert to hex

def convert_base10_int_to_binary(int_num) -> string: 
    '''
    Returns binary string value from integer base 10 numbers.
    '''
    
    pass

def convert_base10_fraction_to_binary(fract_num) -> string: 
    '''
    Returns binary string value from fractional base 10 numbers. Includes decimal.
    '''
    pass
