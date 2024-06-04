"""Generate sample data for the products table and test data for JMeter"""

import faker as Faker


def generate_sample_data():
    """Generate sample data for the products table"""
    fake = Faker.Faker()

    # Generate sample product data
    sample_data = [(fake.word(), fake.random_number(digits=3)) for _ in range(1000)]

    # Write sample data to a file
    with open("sample_data.sql", "w", encoding="utf-8") as file:
        for name, price in sample_data:
            file.write(
                f"INSERT INTO products (name, price) VALUES ('{name}', {price});\n"
            )

    return sample_data


def generate_test_data():
    """Generate test data for JMeter"""
    fake = Faker.Faker()

    # Call generate_sample_data() function to generate sample data
    sample_data = generate_sample_data()

    # Generate test data for get products functionality
    with open("get_products_test_data.csv", "w", encoding="utf-8") as file:
        file.write("name,price\n")
        for name, price in sample_data[:100]:
            file.write(f"{name},{price}\n")

    # Generate test data for add product functionality
    with open("add_product_test_data.csv", "w", encoding="utf-8") as file:
        file.write("name,price\n")
        for _ in range(100):
            name = fake.word()
            price = fake.random_number(digits=3)
            file.write(f"{name},{price}\n")

    # Generate test data for delete product by id functionality
    with open("delete_product_test_data.csv", "w", encoding="utf-8") as file:
        file.write("id\n")
        for id_ in range(1, 11):
            file.write(f"{id_}\n")

    # Generate test data for update product functionality
    with open("update_product_test_data.csv", "w", encoding="utf-8") as file:
        file.write("id,name,price\n")
        for id_, (name, price) in enumerate(generate_sample_data()[50:60], start=50):
            file.write(f"{id_},{name},{price}\n")


def main():
    """Main function"""
    generate_sample_data()
    generate_test_data()


if __name__ == "__main__":
    main()
