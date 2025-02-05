from persistence import *


def print_table(table_name: str, rows: list):
    print(table_name)
    for row in rows:
        print(row)


def print_detailed_employees_report():
    query = """
    SELECT e.name, e.salary, b.location, 
           IFNULL(SUM(ABS(a.quantity) * p.price), 0) AS total_sales_income
    FROM employees e
    JOIN branches b ON e.branche = b.id
    LEFT JOIN activities a ON e.id = a.activator_id AND a.quantity < 0
    LEFT JOIN products p ON a.product_id = p.id
    GROUP BY e.id
    ORDER BY e.name
    """
    rows = repo.execute_command(query)
    print("Employees Report")
    for row in rows:
        print(" ".join(map(str, row)))


def print_detailed_activities_report():
    query = """
    SELECT a.date, p.description, a.quantity, 
           CASE WHEN a.quantity < 0 THEN e.name ELSE NULL END AS seller_name,
           CASE WHEN a.quantity > 0 THEN s.name ELSE NULL END AS supplier_name
    FROM activities a
    JOIN products p ON a.product_id = p.id
    LEFT JOIN employees e ON a.activator_id = e.id
    LEFT JOIN suppliers s ON a.activator_id = s.id
    ORDER BY a.date
    """
    rows = repo.execute_command(query)
    print("Activities Report")
    for row in rows:
        print(row)


def main():
    print_table("Activities", repo.execute_command(
        "SELECT * FROM activities ORDER BY date"))
    print_table("Branches", repo.execute_command(
        "SELECT * FROM branches ORDER BY id"))
    print_table("Employees", repo.execute_command(
        "SELECT * FROM employees ORDER BY id"))
    print_table("Products", repo.execute_command(
        "SELECT * FROM products ORDER BY id"))
    print_table("Suppliers", repo.execute_command(
        "SELECT * FROM suppliers ORDER BY id"))
    print_detailed_employees_report()
    print_detailed_activities_report()


if __name__ == '__main__':
    main()
