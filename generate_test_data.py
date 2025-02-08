import re
import json
import random
import string
from faker import Faker

# Initialize Faker for realistic data generation
fake = Faker()

# Helper Functions

def generate_email():
    """Generate a valid email address."""
    return fake.email()

def generate_name():
    """Generate a realistic full name."""
    return fake.name()

def generate_phone_number():
    """Generate a valid phone number."""
    return fake.phone_number()

def generate_location():
    """Generate a random location (city, country)."""
    return {
        "city": fake.city(),
        "country": fake.country()
    }

def generate_password(length=12):
    """Generate a random secure password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def validate_email(email):
    """Validate email using regex."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

# Generate Test Data
def generate_test_data(num_records=10):
    """Generate a dataset with multiple test records."""
    dataset = []
    for _ in range(num_records):
        record = {
            "name": generate_name(),
            "email": generate_email(),
            "phone_number": generate_phone_number(),
            "location": generate_location(),
            "password": generate_password()
        }
        dataset.append(record)
    return dataset

# Save Dataset to JSON 
def save_to_json(data, filename="test_data.json"):
    """Save generated data to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4) 

# Main block to execute the script
if __name__ == "__main__": 
    # Number of records to generate
    num_records = 12 

    # Generate test data
    test_data = generate_test_data(num_records)

    # Save to JSON
    save_to_json(test_data) 

    print(f"Generated {num_records} test data records and saved to 'test_data.json'.") 
