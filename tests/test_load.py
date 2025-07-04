import pytest
import csv
from etl.load import Load

loader = Load('output')

def test_created_to_csv_success(tmp_path):
    users = [
    {
        "id": "123456",
        "name": "JOHN DOE",
        "email": "john@example.com",
        "full_address": "123 Main St, Illinois, Springfield, 12345"
    },
    {
        "id": "7891011",
        "name": "JANE SMITH",
        "email": "jane@example.com",
        "full_address": "456 Oak Ave, Metropolis, Metropolis, 54321"
    }
]
    file = tmp_path / 'test_users_cleaned.csv'

    loader.load_file(users, str(file))
    # Check if the file was created
    assert file.exists()

def test_load_to_csv_file_content(tmp_path):
    users = [
    {
        "id": "11111111",
        "name": "JOHN DOE",
        "email": "john@example.com",
        "full_address": "123 Main St, Illinois, Springfield, 12345"
    }
]
    file = tmp_path / 'test_users_cleaned.csv'
    loader.load_file(users, str(file))
    assert file.exists()
    # Check if the file has the correct content
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) == 1
    assert rows[0]['id'] == '11111111'
    assert rows[0]['email'] == 'john@example.com'
    assert rows[0]["name"] == "JOHN DOE"
    assert rows[0]['full_address'] == '123 Main St, Illinois, Springfield, 12345'