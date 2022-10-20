import random
random.seed(random.randint(0, 100000))

def find_min(a):
    min_index = 0
    for i in range(0, len(a)):
        if a[i] < a[min_index]:
            min_index = i
    return(a[min_index])

def create_random_arr():
    a = []

    while True:
        try:
            while True:
                size = int(input("Введите длину случайного массива:"))
                if size > 0:
                    break
                else:
                    print("ниче не понял\n")
            break
        except:
            print("мне надо ЧИСЛО >:/\n")

    while True:
        try:
            min_num = int(input("Введите МИНИМАЛЬНО возможный случайный элемент:"))
            max_num = int(input("Введите МАКСИМАЛЬНО возможный случайный элемент:"))
            if max_num >= min_num:
                break
            else:
                print("обычно максимальный элемент больше минимального, ну или хотя бы равен ему\n")
        except:
            print("хочу ЧИСЛО! >:/\n")

    for i in range(size+1):
        a.append(random.randint(min_num, max_num))
    return a

choice = 0
arr = []

while True:
    print("Ку, Вы хотите рандомный массив (введите 1)\nили наберёте сами? (введите 2)\n(а ещё давайте без дробных чисел, разработчики не завезли фишку с ними)")
    while True:
        try:
            choice = int(input())
            break
        except:
            print("это не число...\n")


    if choice == 1:
        arr = create_random_arr()
        break

    elif choice == 2:
        while True:
            try:
                print("Введите числа через пробел:")
                str = input()
                arr = list(map(int, str.split()))
                break
            except:
                print("чета как-то коряво получилось, ну-ка ещё раз\n")
        break

    else:
        print("ОДИН или ДВА!!!!!!!! >:/\n")

print("Ваш массив: \n", arr)

while True:
    try:
        delta = abs(int(input("Введите дельту (если введёте отрицательное число, то я просто возьму модуль :/)\n")))
        break
    except:
        print("циферки надо\n")

arr_min = find_min(arr)
ans = []

for i in range(0, len(arr)):
    if abs(arr_min - arr[i]) == delta:
        ans.append(arr[i])

print("Всего найден(о)", len(ans), "элемент(ов/a), отличающи(й/x)ся от", arr_min, "на", delta, ".")