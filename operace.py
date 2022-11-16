# 5 + 5         sčítání
# 5 - 5         odčítání
# 5 / 5         dělení
# 5 // 5        floor dělení
# 5 % 5         zbytek
# 5 ** 5        mocnina
# 5 ** (1/5)    odmocnina

try:
    inuput("hi")  # červená = syntax špatně
    input( "hi")  # žlutá = formátování špatně
    input("melo")  # zelená = spelling špatně


    x, y, z = 1, 2, 3  # nastavení více proměnných najednou


    str(1)          # "1"
    int("8")        # 8
    float(5)        # 5.0
    bool("false")   # false


    type(promenna)              # vrati typ
    isinstance(promena, int)    # je to daný typ?


    i = 2.5
    int(i)          # 2
    round(i, 0)     # 3.0


    #  bool = False    proměnná se nesmí názvem shodovat s funkcí nebo definicí
    #  True = 1
    #  input = "hello"

finally:
    print(
        "Tvoje " +
        "mama"
    )
    print("""Tvoje
mama"""
    )

    print("fuck u  " * 10)


    bod, x, y = "A", 100, 200
    print("Bod " + bod + " se nachazi na souradnicich [" + x + ", " + y + "]")
    print(f"Bod {bod} se nachazi na souradnicich [{x}, {y}]")
