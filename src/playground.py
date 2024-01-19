def main():
    a = ["aaa","aab","bc","aaabbcc"]

    a.sort(key=lambda w: len(w), reverse=True)
    print(a)


if __name__ == "__main__":
    main()
