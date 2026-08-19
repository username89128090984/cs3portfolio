while True:
    try:
        year = int(input("In what year were you born? "))
    except ValueError:
        print("Please enter an integer.")
        continue
    else:
        break

if year < 1900:
    print("This program only works with years later than (or equal to) 1900.")
else:
    signs = ["Rat (鼠 / Shǔ)",
             "Ox (牛 / Niú)",
             "Tiger (虎 / Hǔ)",
             "Rabbit (兔 / Tù)",
             "Dragon (龙 / Lóng)",
             "Snake (蛇 / Shé)",
             "Horse (马 / Mǎ)",
             "Goat (羊 / Yáng)",
             "Monkey (猴 / Hóu)",
             "Rooster (鸡 / Jī)",
             "Dog (狗 / Gǒu)",
             "Pig (猪 / Zhū)"]

    sign = signs[(year - 4) % 12]

    print(f"Your Chinese Zodiac sign is the {sign}.")