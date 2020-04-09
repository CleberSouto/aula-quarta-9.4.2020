v_lata = 80
print('Digite o tamanho da área em metros quadrados')
area = float(input())
l_lata = 18
litros = area / 3
q_lata = round(litros / l_lata+ 0.5) 
v_total = v_lata * q_lata
print('A quantidade de latas são: ',q_lata)
print('O valor da quantidade de latas é:R$ ', v_total)