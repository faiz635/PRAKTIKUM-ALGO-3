# print("=========Selamat Datang di Segitiga Detektor =========")

# a = int(input(" Masukan sisi a : "))
# b = int(input(" Masukan sisi b : "))
# c = int(input(" Masukan sisi b : ")) 
# if a + b > c and a + c > b and b + a > a : 
  # if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 : 
    # print("segitiga siku siku") 
  # elif a == b == c: 
    # print("segitiga sama sama sisi ")    
  # elif  a==b or b==c or a==c : 
    # print("segitiga sama kaki") 
  # else : 
    # print ("segitiga sembarang") 
# else: 
  # print("Ini bukan segitiga")

# print("=========Terima Kasih =========")



import math

nilai1 = int(input("Masukan Nilai A = "))
nilai2 = int(input("Masukan Nilai B = "))
nilai3 = int(input("Masukan Nilai C = "))
if nilai1 == 0:
 print("Bukan merupakan Persamaan Kuadrat")
else:
 D = (nilai2**2) - (4*nilai1*nilai3)
if D > 0:
 x1 = (-nilai2 + math.sqrt(D)) / (2*nilai1)
 x2 = (-nilai2 - math.sqrt(D)) / (2*nilai1)
 print("Persamaan kuadrat ", nilai1, "x^2", "+", nilai2, "x", "+", (nilai3))
 print("Determinan = ", D)
 print("Akar x1 = ", x1)
 print("Akar x2 = ", x2)
 print("Dua akar berbeda") 

elif D == 0:
 x1 = (-nilai2 + math.sqrt(D)) / (2*nilai1)
 x2 = (-nilai2 - math.sqrt(D)) / (2*nilai1)
 print("Persamaan kuadrat ", nilai1, "x^2", "+", nilai2, "x", "+", (nilai3))
 print("Determinan = ", D)
 print("Akar = ", x1 or x2)
 print("Dua akar kembar") 

elif D < 0:

 print("Persamaan kuadrat ", nilai1, "x^2", "+", nilai2, "x", "+", (nilai3))
 print("Determinan = ", D)
 print("Akar x1 = -", (nilai2), "+ √",(D), "/ 2*", (nilai1))
 print("Akar x2 = -", (nilai2), "- √",(D), "/ 2*", (nilai1))
 print("Tidak mempunyai akar") 

