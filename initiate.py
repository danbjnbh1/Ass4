from persistence import *

import sys
import os


def add_branche(splittedline: list[str]):
    branch_id = int(splittedline[0])
    location = splittedline[1]
    number_of_employees = int(splittedline[2])
    repo.branches.insert(Branche(branch_id, location, number_of_employees))


def add_supplier(splittedline: list[str]):
    supplier_id = int(splittedline[0])
    name = splittedline[1]
    contact_information = splittedline[2]
    repo.suppliers.insert(Supplier(supplier_id, name, contact_information))


def add_product(splittedline: list[str]):
    product_id = int(splittedline[0])
    description = splittedline[1]
    price = float(splittedline[2])
    quantity = int(splittedline[3])
    repo.products.insert(Product(product_id, description, price, quantity))


def add_employee(splittedline: list[str]):
    employee_id = int(splittedline[0])
    name = splittedline[1]
    salary = float(splittedline[2])
    branch_id = int(splittedline[3])
    repo.employees.insert(Employee(employee_id, name, salary, branch_id))


adders = {"B": add_branche,
          "S": add_supplier,
          "P": add_product,
          "E": add_employee}


def main(args: list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])


if __name__ == '__main__':
    main(sys.argv)
