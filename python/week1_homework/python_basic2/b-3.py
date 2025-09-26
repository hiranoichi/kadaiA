rows = int(input("行数を入力してください: "))
cols = int(input("列数を入力してください: "))

for j in range(1, rows + 1):
    for i in range(1, cols + 1):
        result = i * j

        print(f"{i} x {j} = {result:2} | ", end="")
    print()
