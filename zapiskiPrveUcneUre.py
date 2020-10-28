a=int(input("št a:"))
b=int(input("št b:"))

#input() ti da v string aka besedilo
#če ne bi tipizirali (to smo naredili z int()) bi seštevanje šlo skozi
#ampak bi za a=4 in b=7 dobili a+b==47
#podobno kot a="H" in b="ello" bi a+b == "Hello"


# x = <>
# je prirejanje spremenjivki z imenom x temu kar bi napisali namesto <>
# <> je lahko 
#   celo število (int)
#   decimalno število (float) (ali pa double. Odvisno od števila decimalk. Samo to vam na tej točki bolj malo pove.)
#   besedilo (string oz str)
#   True ali False (boolean oz bool)

# x == <>
#je pa gledanje ali je to kar imamo shranjeno v spremenjivki x enako temu kar bi napisali namesto <>

ime = "Monty"
print("Moje ime je", ime)
print("Moje ime je" + ime)


#komenitiranje enega stavka je tukaj lepo prikazano. S tem da začneš z #

primer="kometiraš lahko tudi v isti vrstici kot je uporabna koda" #kot vidiš 

#druga opcija je večvrstično komenitiranje z """
"""tko
neki drugače to lahko prikaže oz druga barvna shema kot komentiranje z #
recimo jaz ko tole pišem se mi piše črno na zelo temno ozadje
"""


#python je zelo občutljiv na to kako zamaknjena je koda aka tab (nad caps lock, tista tipka k ima narisan ->)
    #fun fact 1 tab je enako 4 presledkom
    #je pa veliko hitreje če samo tab pritisneš

#ta koda za primer ko je a večji od b
print()
if(a<b):
    print("a je manjše od b")
else:
    if(a==b):
        print("a je enako b")
    print("konec else prvega if primera muahahaha")

print("\nkonec prvega if primera\n")
#fun fact \n v stingu (torej med "") pove da doda novo vrstico pri izpisu (kot da bi dodaten ENTER kliknu)

#in koda nista enaki za primer ko je a večji od b

print("drugi primer, ki ti pokaže pomembnost pravilnosti tabov\n")
if(a<b):
    print("a je manjše od b")
else:
    if(a==b):
        a=b #samo zato ker prevajalnik zahteva da neki je v if stavku. Drugače joka da je neki narobe.        
    print("a je enako b")
    print("konec else drugega if primera muahahaha")

print("\nkonec drugega if primera\n\n")  
    

print("drugi primer, ki prikaže pomembnost pravilnih tabov\n")
leto = int(input("Prosim vpiši letnico: "))

print("Če so tabi narobe postavljeni\n")
if leto % 4 == 0:
    print("prestopno leto")
if leto % 100 == 0: 
    print("ni prestopno")
else: print("ni prestopno")

print("\nČe so tabi pravilno postavljeni\n")

if leto % 4 == 0:
    print("prestopno leto")
    if leto % 100 == 0: 
        print("ni prestopno")
else: print("ni prestopno")

print("\nMatematika\n")
print(type(a))

print("sestevanje", a+b)
print("razlika", a-b)
print("množenje", a*b)
print("deljenje", a/b)
print("ostanek", a%b)
print("celoštevične deljenje", a//b)
print("potenciranje", a**b)

#if in elif

print("\nif in elif primera\n")  
#recimo če bi imeli

if a<20:
	print("manjše kot 20")
if a<25:
	print("med 20 in 25")
if a<50:
	print("med 25 in 50")


#in če bi dal a = 15 bi ti vse tri izpisalo


#če bi uporabil elif
print("\nČe se uporabi elif\n")
if a<20:
	print("manjše kot 20")
elif a<25:
	print("med 20 in 25")
elif a<50:
	print("med 25 in 50")
	
#in je a = 15 
#bi se ti izpisalo samo prvo
#torej manjše kot 20