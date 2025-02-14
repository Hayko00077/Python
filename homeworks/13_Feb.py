# Տրված 10-ական համակարգի թվերը բերել երկուական և չորսական տեսքի՝ 
# երկուական կոդի արդյունքը արտահայտել 10 բիթով։
# { 83 , 266 , -61 , 482 , -139 ,-10, 57, -124, -57, -3, 47 }

def decimal_to_binary(n, bits=10):
    binary = ''
    if n == 0:
        return '0'
    if n > 0:
        while n != 0:
            binn = n % 2
            binary = str(binn) + binary
            n = n // 2

        while len(binary) < bits:
            binary = '0' + binary
        return binary
    
    if n < 0:
        n = -n
        while n != 0:
            binn1 = n % 2
            binary = str(binn1) + binary
            n = n // 2
        
        binary_list = list(binary)
        for i in range(0, len(binary_list)):
            if binary_list[i] == '0':
                binary_list[i] = '1'
            elif binary_list[i] == '1':
                binary_list[i] = '0'
        
        carry = 1
        for i in range(len(binary_list) -1, -1, -1):
            if binary_list[i] == '0' and carry == 1:
                binary_list[i] = '1'
                carry = 0
            elif binary_list[i] == '1' and carry == 1:
                binary_list[i] = '0'

        binary = ''.join(binary_list)
        while len(binary) < bits:
            binary = '1' + binary
        return binary


def binary_to_decimal(binary_str):
    decimal = 0
    for bit in binary_str:
        decimal = decimal * 2 + int(bit)
    return decimal

def decimal_to_quaternary(n):
    if n == 0:
        return '0'
    quaternary = decimal_to_binary(n)
    quaternary_list1 = []
    quaternary_list = list(quaternary)
    

    for i in range(len(quaternary_list) // 2):
        chlp = quaternary_list[i * 2:i * 2 + 2]
        decimal_tmp = binary_to_decimal(chlp)

        quaternary_list1.append(str(decimal_tmp))
 

    quaternary = ''.join(quaternary_list1)
    return quaternary


numbers = [83, 266, -61, 482, -139, -10, 57, -124, -57, -3, 47]

for num in numbers:
    binary = decimal_to_binary(num)
    quaternary = decimal_to_quaternary(num)
    print(f"Decimal: {num}\tBinary: {binary}\tQuaternary: {quaternary}")


# Հետևյալ նշանից կախված երկուական թվերը բերել տասական և տասնվեցական տեսքի։
# { 111111111, 100010001, 000010101, 010101111, 110101111, 011110000,   111011000, 010011001 }
print()

def binary_to_decimal(binary_str1):
    decimal = 0
    binary_str1_list = list(binary_str1)
    if binary_str1_list[0] == '0':
        for bit in range(len(binary_str1_list)):
            decimal = decimal * 2 + int(binary_str1_list[bit])
        return decimal

    elif binary_str1_list[0] == '1':
        for i in range(0, len(binary_str1_list)):
            if binary_str1_list[i] == '0':
                binary_str1_list[i] = '1'
            elif binary_str1_list[i] == '1':
                binary_str1_list[i] = '0'

        carry = 1
        for i in range(len(binary_str1_list) -1, -1, -1):
            if binary_str1_list[i] == '0' and carry == 1:
                binary_str1_list[i] = '1'
                carry = 0
            elif binary_str1_list[i] == '1' and carry == 1:
                binary_str1_list[i] = '0'

        for bit in range(len(binary_str1_list)):
            decimal = decimal * 2 + int(binary_str1_list[bit])
        
        decimal = - + decimal
        return decimal
    

def binary_to_hexadecimal(hexadecimal_str1, bits = 12):

    if len(hexadecimal_str1) < bits:
        if hexadecimal_str1[0] == '1':
            while len(hexadecimal_str1) < bits:
                hexadecimal_str1 = '1' + hexadecimal_str1
        
        elif hexadecimal_str1[0] == '0':
            while len(hexadecimal_str1) < bits:
                hexadecimal_str1 = '0' + hexadecimal_str1

    hexadecimal_list = list(hexadecimal_str1)
    hexadecimal = ''
    hexadecimal_list1 = []

    ls = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(len(hexadecimal_list) // 4):
        chlp = hexadecimal_list[i * 4: i * 4 + 4]
        hexadecimal_tmp = binary_to_decimal(chlp)
        hexadecimal_list1.append(ls[hexadecimal_tmp])
    
    hexadecimal = ''.join(hexadecimal_list1)
    return hexadecimal



binary_numbers = ['111111111', '100010001', '000010101', '010101111', '110101111', '011110000', '111011000', '010011001']

for number in binary_numbers:
    decimal = binary_to_decimal(number)
    hexadecimal = binary_to_hexadecimal(number)
    print(f"Binary: {number}\tDecimal: {decimal}\tHexadecimal: {hexadecimal}")