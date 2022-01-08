import hashlib as hasher
import time 
print('-'*30)
print(""" 
     text encryption  
     metin şifreleme
              
instagram: trojan.tht
versiyon: 1.v
      """)
print("-"*30)             
print(""" 
şifreleme türü seçiniz
[1 , 11]md5                 
[2 , 22]sha1                       
[3 , 33]sha224      
[4 , 44]sha256      
[5 , 55]sha384      
[6 , 66]sha3_256      
[7 , 77]sha3_384      
[8 , 88]sha3_512      
[9 , 99]sha512            
      """)
print(time.asctime())
print('-'*30)
time.sleep(2)
secim = int(input("işlem kodu girini: "))
if secim == 1:
  metin = input('metin giriniz: ')
  sifre = hasher.md5()
  sifre.update(metin.encode('utf-8'))
  hash = sifre.hexdigest()
  print(hash)
 
  
elif secim == 11:
  me = input('metin giriniz: ')
  time.sleep(2)
  sifre1 = hasher.sha1()
  sifre1.update(me.encode('utf-8'))
  hash1 = sifre1.hexdigest()
  
  sifre2 = hasher.md5()
  sifre2.update(hash1.encode('utf-8'))
  hash2 = sifre2.hexdigest()
  
  # Farklı algoritmalar kullanarak     çözûlmesini zor hale getiriyorum
 #Böylece güçlü şifreler ortaya çıkar
  
  a = hasher.sha384()
  a.update(hash1.encode('utf-8'))
  b = a.hexdigest()
  print(b)

elif secim == 2:
  l = input("metin geriniz: ")
  time.sleep(1)
  pw = hasher.sha1()
  pw.update(l.encode("utf-8"))
  w = pw.hexdigest()
  print(w)
  
elif secim == 22:
  k = input("metin giriniz: ")
  j = hasher.sha3_256()
  j.update(k.encode('utf-8'))
  q = j.hexdigest()
  
  n = hasher.md5()
  n.update(q.encode('utf-8'))
  _1 = n.hexdigest()
  
  _w = hasher.sha384()
  _w.update(_1.encode('utf-8'))
  b_ = _w.hexdigest()
  print(b_)
  
elif secim == 3:
	zor = input("metin giriniz: ")
	zor_be = hasher.sha224()
#	print(str(zor_be))
	zor_be.update(zor.encode('utf-8'))
	zor_be_ya = zor_be.hexdigest()
	print(zor_be_ya)
	
elif secim == 33:
	tac = input("metin giriniz: ")
	time.sleep(1)
	fatih = hasher.sha512()
	fatih.update(tac.encode('utf-16'))
	ast = fatih.hexdigest()
	
	un = hasher.sha224()
	un.update(ast.encode('utf-8'))
	us = un.hexdigest()
	
	mm = hasher.sha384()
	mm.update(us.encode('utf-8'))
	ml = mm.hexdigest()
	print(ml)
	
elif secim == 4:
	qq = hasher.sha256()
	print(__z := input('metin giriniz: '))
	qq.update(__z.encode('utf-8'))
	q_q = qq.hexdigest()
	print(q_q)
	
elif secim == 44:#elif ile filanca şey ise.falanca şeyi.yap
# eşit ise  yap eşit degilse yapma!!
	e_ = input('metin giriniz ')
	time.sleep(1)# time ile 1 saniye sonra çalîşyo .progam
	ee = hasher.sha512()
	ee.update(e_.encode('utf-16'))
	_e_  = ee.hexdigest()
	
	tt = hasher.md5()
	tt.update(_e_.encode("utf-7"))
	t_t = tt.hexdigest()
	
	k_k = hasher.sha3_512()
	k_k.update(t_t.encode('utf-8'))
	aqa = k_k.hexdigest()
	print(aqa)
	
elif secim == 5:
	o = input('metin giriniz: ')
	time.sleep(1)
	q__w = hasher.sha384()
	q__w.update(o.encode('utf-8'))
	asasd = q__w.hexdigest()
	print(asasd)
	
elif secim == 55:
	_1a = input("metin giriniz: ")
	_2a = hasher.sha384()
	_2a.update(_1a.encode("utf-16"))
	_3a = _2a.hexdigest()
	
	u1 = hasher.sha3_512()
	u1.update(_3a.encode("utf-8"))	
	u3 = u1.hexdigest()
	
	t1 = hasher.sha3_256()
	t1.update(u3.encode("utf-8"))
	t2 = t1.hexdigest()
	print(t2)
	
elif secim == 6:
	m1 = input("metin giriniz: ")
	time.sleep(1)
	m2 = hasher.sha3_256()
	m2.update(m1.encode("utf-8"))
	m3 = m2.hexdigest()
	print(m3)
	
elif secim == 66:
	f1 = input("metin giriniz: ")
	time.sleep(1)
	f2 = hasher.sha224()
	f2.update(f1.encode("utf-8"))
	f3 = f2.hexdigest()
	
	s1 = hasher.md5()
	s1.update(f3.encode('utf-8'))
	s2 = s1.hexdigest()
	
	
	v2 = hasher.sha512()
	v2.update(s2.encode('utf-16'))
	v3 = v2.hexdigest()
	print(v3)
	
elif secim == 7:
	j1 = input("metin giriniz: ")
	j2 = hasher.sha3_384()
	j2.update(j1.encode("utf-8"))
	j3 = j2.hexdigest()
	print(j3)
	
elif secim == 77:
	l1 = input('metin giriniz: ')
	l2 = hasher.sha1()
	l2.update(l1.encode("utf-16"))
	l3 = l2.hexdigest()
	
	l4 = hasher.sha3_512()
	l4.update(l3.encode('utf-8'))
	l5 = l4.hexdigest()
	
	l6 = hasher.md5()
	l6.update(l5.encode('utf-7'))
	l7 = l6.hexdigest()
	
	l8 = hasher.sha1()
	l8.update(l7.encode('utf-16'))
	l9 = l8.hexdigest()
	print(l9)
	
elif secim == 8:
	print(e1 := input("metin giriniz: "))
	e2 = hasher.sha3_512()
	e2.update(e1.encode("utf-8"))
	e3 = e2.hexdigest()
	print(e3)
	
elif secim == 88:
	r1 = input("metin giriniz: ")
	time.sleep(1)
	r2 = hasher.sha3_512()
	r2.update(r1.encode("utf-16"))
	r3 = r2.hexdigest()
	
	r4 = hasher.sha1()
	r4.update(r3.encode("utf-8"))
	r5 = r4.hexdigest()
	
	r7 = hasher.sha512()
	r7.update(r5.encode("utf-16"))
	r8 = r7.hexdigest()
	print(r8)
	
elif secim == 9:
	x1 = input("metin giriniz: ")
	time.sleep(1)
	x2 = hasher.sha512()
	x2.update(x1.encode("utf-8"))
	x3 = x2.hexdigest()
	print(x3)
	
elif secim == 99:
	c1 = input("metin giriniz: ")
	time.sleep(1)
	c2 = hasher.sha384()
	c2.update(c1.encode("utf-16"))
	c3 = c2.hexdigest()
	
	c_1 = hasher.sha512()
	c_1.update(c3.encode("utf-7"))
	c_2 = c_1.hexdigest()
	
	c0 = hasher.sha224()
	c0.update(c_2.encode("utf-16"))
	c9 = c0.hexdigest()
	
	kkv = hasher.sha3_256()
	kkv.update(c9.encode("utf-16"))
	kk1 = kkv.hexdigest()
	print(kk1)
	
	# kullandınız için teşkkürler
	
else:
	print("yanlîş kod yazdınız")
