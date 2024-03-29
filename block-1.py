def run():
    with open('.\\files\\farm.txt', 'r') as farm:
        feet = [int(foot) for foot in farm]

    print("Общее количество ног всех животных", feet[0] * 4 + feet[1] * 4 + feet[2] * 2)


if __name__ == "__main__":
    run()
