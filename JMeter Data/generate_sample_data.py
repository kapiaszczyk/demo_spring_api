"""Generate sample data for the products table and test data for JMeter"""


import faker as Faker


def main():
    """Main function"""

    MAXIMUM_ID = 1000

    fake = Faker.Faker()
    insert_statements = []
    products = {}

    # Create 1000 products
    for _ in range(1000):
        name = fake.word()
        price = fake.random_number(digits=3)
        products[name] = price
        insert_statements.append(f"INSERT INTO products (name, price) VALUES ('{name}', {price});")

    # Write the insert statements to a file
    with open('sample_data.sql', 'w', encoding='utf-8') as file:
        file.write('\n'.join(insert_statements))

    # Generate test data to be used in testing the get products functionality
    with open('get_products_test_data.csv', 'w', encoding='utf-8') as file:
        file.write('name,price\n')
        minimum_id = 100
        # Get products with ids from 100 to 199
        for name, price in products.items():
            if minimum_id <= MAXIMUM_ID:
                file.write(f'{name},{price}\n')
                minimum_id += 1

    # Generate test data to be used in testing the get product by id functionality
    with open('delete_product_test_data.csv', 'w', encoding='utf-8') as file:
        file.write('id\n')
        for num in range(10):
            id_ = 200 + 1
            file.write(f'{id_}\n')

    # Generate test data to be used in testing the add product functionality
    with open('add_product_test_data.csv', 'w', encoding='utf-8') as file:
        file.write('name,price\n')
        for _ in range(100):
            name = fake.word()
            price = fake.random_number(digits=3)
            file.write(f'{name},{price}\n')

    # Generate test data to be used in testing the delete product by id functionality
    with open('delete_product_test_data.csv', 'w', encoding='utf-8') as file:
        file.write('id\n')
        for num in range(10):
            id_ = num + 1
            file.write(f'{id_}\n')

    # Generate test data to be used in testing the update product functionality
    with open('update_product_test_data.csv', 'w', encoding='utf-8') as file:
        file.write('id,name,price\n')
        for num in range(10):
            id_ = num + 50
            name = fake.word()
            price = fake.random_number(digits=3)
            file.write(f'{id_},{name},{price}\n')

if __name__ == '__main__':
    main()
