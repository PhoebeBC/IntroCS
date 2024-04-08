
import csv
import random
from faker import Faker

fake = Faker()


# Generate fake customer data
def generate_fake_customers(num_customers):
    customers = []
    for _ in range(num_customers):
        customer = {
            'Name': fake.name(),
            'Email': fake.email(),
            'Phone': fake.phone_number(),
            'Address': fake.address(),
            'Company': fake.company(),
            'Job Title': fake.job(),
            'Age': random.randint(18, 80),
            'Gender': random.choice(['Male', 'Female']),
            'Income': round(random.uniform(20000, 150000), 2)
        }
        customers.append(customer)
    return customers


# Write fake customer data to CSV file
def write_fake_customer_data(customers, filename):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Name', 'Email', 'Phone', 'Address', 'Company', 'Job Title', 'Age', 'Gender', 'Income']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for customer in customers:
            writer.writerow(customer)


# Generate 100 fake customers and write to CSV file
fake_customers = generate_fake_customers(100)
write_fake_customer_data(fake_customers, 'fake_customers.csv')
