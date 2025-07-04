import pytest
from etl.transform import Transform

transform = Transform()

# Test cases for is_valid_email function
def test_is_valid_email():
    assert transform.is_valid_email("test@example.com"), "Email válido rechazado"
    assert not transform.is_valid_email("invalid-email")

# Test cases for normalize_name function
def test_normalize_name():
    name = {'name': {
            'first': 'John', 
            'last': 'Doe'}
            }
    assert transform.normalize_name(name) == "JOHN DOE"

def test_normalize_name_with_empty_fields():
    name = {'name': {
            'first': '', 
            'last': 'Doe'}
            }
    assert transform.normalize_name(name) == "DOE"
    
    name = {'name': {
            'first': 'John', 
            'last': ''}
            }
    assert transform.normalize_name(name) == "JOHN"
    
def test_normalize_name_with_spaces():
    name = {'name': {
            'first': '  John  ', 
            'last': '  Doe  '}
            }
    assert transform.normalize_name(name) == "JOHN DOE"
 
# Test cases for normalize_address function
def test_normalize_address():
    user = {'location': {
            'street': {
                'number': 123, 
                'name': 'Main St'
            },
            'city': 'Mérida', 
            'state': 'Yucatán', 
            'postcode': '97000'
            }
        }
    assert transform.normalize_address(user) == "123 Main St, Yucatán, Mérida, 97000"

#Test validate unique IDs
def test_transform_unique_ids_and_filter():
    users = [
        {'login': {
            'uuid': '1'
            }, 
            'email': 'test@example.com', 
            'name': {
                'first': 'A',
                'last': 'B'
                },
            'location': {
                'street': {
                    'number': 1,
                    'name': 'S'
                    }, 
                'city': 'C', 
                'state': 'D', 
                'postcode': '1'
                }
            },
        {'login': {
            'uuid': '1'
            }, 
            'email': 'test@example.com', 
            'name': {
                'first': 'A',
                'last': 'B'
                },
            'location': {
                'street': {
                    'number': 1,
                    'name': 'S'}, 
                    'city': 'C', 
                    'state': 'D', 
                    'postcode': '1'
                    }
                },
        {'login': {
            'uuid': '2'
            }, 
            'email': 'invalid',
            'name': {
                'first': 'X',
                'last': 'Y'
                },
            'location': {
                'street': {
                    'number': 2,
                    'name': 'T'
                    }, 
                'city': 'U', 
                'state': 'V', 
                'postcode': '2'}}
    ]
    result = transform(users)
    assert len(result) == 1
    assert result[0]['id'] == '1'
