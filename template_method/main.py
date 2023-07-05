from template_method.display import CharDisplay, StringDisplay


def main():
    d1 = CharDisplay("O")
    d2 = StringDisplay("Oh my god")
    d1.display()
    d2.display()


if __name__ == "__main__":
    main()