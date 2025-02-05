from persistence import *

import sys


def apply_action(splittedline: list[str]):
    product_id = int(splittedline[0])
    quantity = int(splittedline[1])
    activator_id = int(splittedline[2])
    date = splittedline[3]

    if quantity == 0:
        return  # Illegal action, do nothing

    print("Applying action: ", splittedline)
    print("Product id:", product_id)
    products = repo.products.find(id=product_id)
    if not products:
        return
    product = products[0]
    if quantity < 0:  # Sale
        if product.quantity + quantity < 0:
            return  # Not enough product to sell
    product.quantity += quantity
    repo.products.update(product)
    repo.activities.insert(Activitie(product_id, quantity, activator_id, date))


def main(args: list[str]):
    inputfilename: str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(", ")
            apply_action(splittedline)


if __name__ == '__main__':
    main(sys.argv)
