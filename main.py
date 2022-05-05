def kopaytma(*sonlar):
  """Sonlarning ko'paytmasini xisoblash"""
  yigindi=1
  for son in sonlar:
    yigindi*=son
  return yigindi

print(kopaytma(1,2,3,45,4))

def talabalar(ism,familiya, **malumotlar):
  """Talabalar xaqida malumotlar yigish"""
  malumotlar['ism']=ism
  malumotlar['familiya']=familiya
  return malumotlar

talaba1=talabalar('ali','abdulloh')
print(talaba1)