#КЕГЭ 20813
#дефолтный представитель регулярок, слэнговое название "арифметическое выражение"

from re import*
a = open('24_20813 (1).txt').readline()
num = r'([789][0789]*|0)'
reg = rf'{num}([-*]{num})*'
reg = rf'(?=({reg}))'
m = (max((x.group(1) for x in finditer(reg, a)), key=len))
print(len(m))
