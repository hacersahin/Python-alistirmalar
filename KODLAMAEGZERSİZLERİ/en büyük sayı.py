"""
Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""
a = int( input("a:"))
b = int( input("b:"))
c = int( input("c:"))

if ( a>=b and a>=c ):
    print( "En Büyük Sayı:",a )
elif ( b>=a and b>=c):
    print( "En Büyük Sayı:",b )
elif ( c>=a and c>=b ):
    print( "En Büyük Sayı:",c )