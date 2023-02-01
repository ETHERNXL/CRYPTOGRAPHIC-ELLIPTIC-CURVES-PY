import datetime

def lyambdaod(x1, y1, p, a):
    l=((3*pow(x1, 2)+a)*(pow((2 * y1), (p-1-1))))%p
    return l

def lyambdaraz(x1, y1, x2, y2, p):
    l=((y2-y1)*pow((x2-x1), (p-1-1)))%p
    return l

def odraz(x1, x2, y1, y2, p, a):
    if x1==x2 and y1==y2:
        l=lyambdaod(x1, y1, p, a)
    else:
        l=lyambdaraz(x1, y1, x2, y2, p)
    return l

def x(l, x1, x2, p):
    x3=(pow(l, 2)-x1-x2)%p
    return x3

def y(l, x1, x3, y1, p):
    y3=(l*(x1-x3)-y1)%p
    return y3

def encdec(n, G, p, a, rYb, rG, kb):
    x1=G[0]
    y1=G[1]
    x2=G[0]
    y2=G[1]
    for i in range(n-1):
        l=odraz(x1, x2, y1, y2, p, a)
        x3=x(l, x1, x2, p)
        y3=y(l, x1, x3, y1, p)
        x2=x3
        y2=y3
    Pm=(x3, y3)
    print("Pm = ", Pm)
    #R=Pm+rYb
    x1=Pm[0]
    y1=Pm[1]
    x2=rYb[0]
    y2=rYb[1]
    l=odraz(x1, x2, y1, y2, p, a)
    x3=x(l, x1, x2, p)
    y3=y(l, x1, x3, y1, p)
    R=(x3, y3)
    print("R = ", R)
    C=(rG, R)
    print("Криптограма: ", C)
    print("Дешифрування:")
    #kb*rG
    x1=rG[0]
    y1=rG[1]
    x2=rG[0]
    y2=rG[1]
    for i in range(kb-1):
        l=odraz(x1, x2, y1, y2, p, a)
        x3=x(l, x1, x2, p)
        y3=y(l, x1, x3, y1, p)
        x2=x3
        y2=y3
    kbrG=(x3, y3)
    print("kb*rG = ", kbrG)
    #R-kbrG
    x1=R[0]
    y1=R[1]
    x2=kbrG[0]
    y2=-kbrG[1]
    l=odraz(x1, x2, y1, y2, p, a)
    x3=x(l, x1, x2, p)
    y3=y(l, x1, x3, y1, p)
    poch=(x3, y3)
    print("Розшифроване: ", poch)
      
        
def main():
    M="BEZPALYI"
    p=751
    a=-1
    b=1
    E=(-1, 1)
    G=(0, 1)
    ka=15
    kb=4
    print("Значення за варіантом:")
    print("Повідомлення: ", M)
    print("p = ", p)
    print("a = ", a)
    print("b = ", b)
    print("E = ", E)
    print("y^2=((x^3)-x+1)mod751")
    print("G = ", G)
    print("ka = ", ka)
    print("kb = ", kb)
    print("--------------------")
    print("Обчислення:")
    #рахуємо Ya:
    x1=G[0]
    y1=G[1]
    x2=G[0]
    y2=G[1]
    for i in range(ka-1):
        l=odraz(x1, x2, y1, y2, p, a)
        x3=x(l, x1, x2, p)
        y3=y(l, x1, x3, y1, p)
        x2=x3
        y2=y3
    Ya=(x3, y3)
    print("Відкритий ключ користувача A: Ya = ", Ya)
    #рахуємо Yb:
    x1=G[0]
    y1=G[1]
    x2=G[0]
    y2=G[1]
    for i in range(kb-1):
        l=odraz(x1, x2, y1, y2, p, a)
        x3=x(l, x1, x2, p)
        y3=y(l, x1, x3, y1, p)
        x2=x3
        y2=y3
    Yb=(x3, y3)
    print("Відкритий ключ користувача B: Yb = ", Yb)
    print("Шифрування:")
    r=int(input("Введіть випадкове ціле число r: "))
    #рахуємо rG:
    x1=G[0]
    y1=G[1]
    x2=G[0]
    y2=G[1]
    for i in range(r-1):
        l=odraz(x1, x2, y1, y2, p, a)
        x3=x(l, x1, x2, p)
        y3=y(l, x1, x3, y1, p)
        x2=x3
        y2=y3
    rG=(x3, y3)
    print("rG = ", rG)
    #рахуємо rYb:
    x1=Yb[0]
    y1=Yb[1]
    x2=Yb[0]
    y2=Yb[1]
    for i in range(r-1):
        l=odraz(x1, x2, y1, y2, p, a)
        x3=x(l, x1, x2, p)
        y3=y(l, x1, x3, y1, p)
        x2=x3
        y2=y3
    rYb=(x3, y3)
    print("rYb = ", rYb)
    
    n=ord("B")
    print("**************************************************")
    print("Буква B - ", n)
    encdec(n, G, p, a, rYb, rG, kb)
    n=ord("E")
    print("**************************************************")
    print("Буква E - ", n)
    encdec(n, G, p, a, rYb, rG, kb)
    n=ord("Z")
    print("**************************************************")
    print("Буква Z - ", n)
    encdec(n, G, p, a, rYb, rG, kb)
    n=ord("P")
    print("**************************************************")
    print("Буква P - ", n)
    encdec(n, G, p, a, rYb, rG, kb)
    n=ord("A")
    print("**************************************************")
    print("Буква A - ", n)
    encdec(n, G, p, a, rYb, rG, kb)
    n=ord("L")
    print("**************************************************")
    print("Буква L - ", n)
    encdec(n, G, p, a, rYb, rG, kb)
    n=ord("Y")
    print("**************************************************")
    print("Буква Y - ", n)
    encdec(n, G, p, a, rYb, rG, kb)
    n=ord("I")
    print("**************************************************")
    print("Буква I - ", n)
    encdec(n, G, p, a, rYb, rG, kb)
    print("**************************************************")


main()