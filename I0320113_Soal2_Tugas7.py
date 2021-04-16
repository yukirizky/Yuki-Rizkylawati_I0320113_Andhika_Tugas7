# perhitungan mencari perpindahan yuki berlari
import math
print("1. Yuki berlari ke arah selatan sejauh 6 meter. \nKemudian belok ke arah timur sejauh 8 meter. \nBerapakah perpindahan yang dialami yuki?")
a = 6
b = 8
c = a ** 2 + b **2
print("perpindahan yuki= ", math.sqrt(c))

# mencari nilai terbesar dan terkecil dari nilai UTS yuki
print("\n2. Setelah menjalani UTS selama sepekan,Yuki telah mengetahui nilainya. kalkulus mendapat 87, biologi mendapat 90, dan programa komputer mendapat 98.")
kalkulus = 87
biologi = 90
progkom = 98
print("nilai tertinggi yang didapat yuki= ", max(kalkulus,biologi,progkom))
print("nilai terendah yang didapat yuki= ", min(kalkulus,biologi,progkom))

# mencari harga mutlak suatu nilai
p = -999
q = -81
r = 49
print("\n3. Tentukan harga mutlak bilangan dibawah ini!")
print("p= ", p)
print("q= ", q)
print("r= ", r)
print("\n|p|= ", abs(p))
print("|q|= ", abs(q))
print("|r|= ", abs(r))

