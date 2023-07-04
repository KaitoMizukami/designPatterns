from adaptor.print_banner import PrintBanner


def main():
    p = PrintBanner('Hello')
    p.print_strong()
    p.print_weak()


if __name__ == '__main__':
    main()