import time


class Sabiranje:
    def __call__(self, a, b):
        return a + b


def stampac(func):
    def odstampana_func(a, b):
        print(f"Ulazni parametri su {a} i {b}")
        return func(a, b)

    return odstampana_func


def kesiranje(func):
    print("Sada je u kesiranju")
    parameters = {}

    def new_func(a, b):
        if (a, b) not in parameters:
            parameters[(a, b)] = func(a, b)
        return parameters[(a, b)]

    return new_func


def vreme(func):
    def nova_funkcija(a, b):
        start_time = time.time()
        res = func(a, b)
        end_time = time.time()
        vreme_izvrsenja = end_time - start_time
        print(f"Vreme izvrsenja : {vreme_izvrsenja} ")
        return res

    return nova_funkcija


@vreme
@kesiranje
def oduzimanje(a, b):
    time.sleep(1)
    return a - b


def main():
    # sub = Sabiranje()
    # print(Sabiranje()(1, 2))
    # start_time = time.time()
    print(oduzimanje(5, 2))
    print(oduzimanje(5, 2))
    print(oduzimanje(3, 1))
    print(oduzimanje(5, 2))
    print(oduzimanje(3, 1))
    print(oduzimanje(5, 2))
    # print(f"Vreme izvrsenja: {time.time() - start_time}")


if __name__ == "__main__":
    main()
