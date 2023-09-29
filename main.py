pay = float(input("Amount need to pay: "))
given = float(input("Amount given: "))

change = round(given - pay, 2)

print("Change: ", change)

changes: dict[str, float] = {
    "20": 0,
    "10": 0,
    "5": 0,
    "2": 0,
    "1": 0,
    "0.25": 0,
    "0.1": 0,
    "0.05": 0
}


changes["20"] = change // 20
change %= 20

changes["10"] = change // 10
change %= 10

changes["5"] = change // 5
change %= 5

changes["2"] = change // 2
change %= 2

changes["1"] = change // 1
change %= 1

changes["0.25"] = change // 0.25
change %= 0.25

changes["0.1"] = change // 0.1
change %= 0.1

changes["0.05"] = change // 0.05
change %= 0.05

if change > 0:
    changes["0.05"] += 1
    change = 0


for amount, bills in changes.items():
    if bills > 0:
        print(f"{bills} x ${amount}")
