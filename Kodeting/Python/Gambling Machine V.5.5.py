import random

m = 1000

while m > 0:
  a = int(input("Hvor mye skal du satse?"))
  if a > m:
    print("Du er i gjeld, balle fjerning i morra. (Og henretting).")
    m = 0
  else:
    m = m - a
    b = int(input("Skriv et tall mellom 1 og 10"))
    c = random.randint(1,10)
    d = random.randint(1,100)
    if b == c: 
      print("Gratulerer, du vant.")
      print(c)
      if d == 69:
        m = a*4 + m
        print("Du fikk firedobbelt!!")
      else:
        m = a*2 + m
      print(m)
    else:
      print("Du tapte:(")
      print(c)
      print(m)
    if m <= 0:
      print("Du er tom for penger. Henretting om en uke.")