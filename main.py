FILE_NAME = "./app/files/test_ips.txt"


def main():
    file = open(FILE_NAME, "r")
    for line in file:
        check_line(line)
        print(line, end="")


def check_line(line:str):
    pass
if __name__ == "__main__":
    main()
