
p = 1000

r = 0.07


n_10 = 10
a_10 = p * (1 + r) ** n_10


n_20 = 20
a_20 = p * (1 + r) ** n_20


n_30 = 30
a_30 = p * (1 + r) ** n_30


print(f"After 10 years, you'll have approximately ${a_10:.2f}")
print(f"After 20 years, you'll have approximately ${a_20:.2f}")
print(f"After 30 years, you'll have approximately ${a_30:.2f}")
