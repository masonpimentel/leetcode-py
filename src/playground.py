def main():
    a = 2

    n = {
        a: 3
    }

    print(n)
    for key, val in n.items():
        print(f'val: {val}, key: {key}')


if __name__ == "__main__":
    main()
