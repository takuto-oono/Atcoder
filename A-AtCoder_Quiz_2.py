





def Jugement(x):
    if 0 <= x < 40:
        return 40 - x

    if 40 <= x < 70:
        return 70 - x

    if 70 <= x < 90:
        return 90 - x

    if x >= 90:
        return 'expert'

def main():
    x = int(input())
    print(Jugement(x))

main()
