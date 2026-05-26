#Write a second function normalize(value, min_val, max_val) that returns (value - min_val) / (max_val - min_val) (This formula is known as-> min-max normalization — you'll use this in ML! — Relax, Aditya sir is yet to cover this 😉 )
#Test it with normalize(50, 0, 100) — should return 0.5

def normalize(value, min_val, max_val):
    x = (value - min_val)/(max_val - min_val)
    return x

a = normalize(50,0,100)
print(a)