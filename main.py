#1
def foydalanuvchi_info(ism, yosh, shahar):
    print(f"Hurmatli {ism}, siz {yosh} yoshdasiz va {shahar}da yashaysiz.")

#2
def statistika(royxat):
    yigindi = sum(royxat)
    orta = yigindi / len(royxat)
    eng_katta = max(royxat)
    
    print(f"Yig‘indi: {yigindi}")
    print(f"O‘rtacha: {orta}")
    print(f"Eng katta: {eng_katta}")

#3
def faktorial(n):
    if n < 0:
        return 0
    
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija

#4
def filtrlash(matn):
    return "".join([x for x in matn if x.isalpha()])

#5
def eng_uzun(matn):
    sozlar = matn.split()
    return max(sozlar, key=len)
