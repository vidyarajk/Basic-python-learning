def tem_convert(temp,unit):
    if unit=='c':
        return temp * 9/5 +32 #c to f
    elif unit=='f':
        return (temp - 32) * 5/9 # f to c
    else:
        return None
    
print(tem_convert(25,"c"))
print(tem_convert(77,"f"))