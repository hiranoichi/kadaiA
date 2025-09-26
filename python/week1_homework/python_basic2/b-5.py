def calc_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def calc_max(numbers):
    max_value = numbers[0]
    for n in numbers:
        if n > max_value:
            max_value = n
    return max_value

def calc_min(numbers):
    min_value = numbers[0]
    for n in numbers:
        if n < min_value:
            min_value = n
    return min_value

def calc_mean(numbers):
    total = calc_sum(numbers)   # 合計は自作関数を利用
    count = 0
    for _ in numbers:
        count += 1
    return total // count  # 平均は整数にしたい場合
    # return total / count # 小数もOKにするならこちら

def main():
    data = input("データを入力してください(スペース区切り) > ")
    numbers = [int(x) for x in data.split()]

    print("合計値:", calc_sum(numbers))
    print("最大値:", calc_max(numbers))
    print("最小値:", calc_min(numbers))
    print("平均値:", calc_mean(numbers))


if __name__ == "__main__":
    main()
