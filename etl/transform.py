import re
import logging
from typing import List, Dict, Any, Set
from email_validator import validate_email, EmailNotValidError

logger = logging.getLogger(__name__)

class Transformer:

    logger.info("Start data transformation process")

    def is_valid_email(self, email: str) -> bool:
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(EMAIL_REGEX.fullmatch(email))
    
    '''
    #This function uses the email_validator library to validate email addresses, it's more extricated and robust.
    def is_valid_email(self, email: str) -> bool:
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False
    '''

    def normalize_name(self, user: Dict) -> str:
        full_name = ''

        # Extracting name components
        if not user:
            logger.warning("User data is empty or None")
            return full_name
        name = user.get('name', {})

        first = name.get('first', '').strip()
        last = name.get('last', '').strip()

        full_name = f"{first} {last}".upper().strip()

        return full_name
    

    def normalize_address(self, user: Dict) -> str:
        full_street = ''

        if not user:
            logger.warning("User data is empty or None")
            return full_street

        # Extracting address components
        location = user.get('location', {})
        street = location.get('street', {})

        number_street = street.get('number', '')
        name_street = street.get('name', '')

        city = location.get('city', '')
        state = location.get('state', '')
        postcode = location.get('postcode', '')

        if number_street and name_street:
            full_street = f"{number_street} {name_street}"

        full_address = []
        
        full_address.append(full_street)
        if state:
            full_address.append(state)
        if city:
            full_address.append(city)
        if postcode:
            full_address.append(str(postcode))

        full_address = ', '.join(part.strip() for part in full_address if part).strip()

        return full_address
    
    def transform(self, users: List[Dict]) -> List[Dict]:

        seen_ids: Set[str] = set()

        transformed = []

        for user in users:
            try:
                # This assumes the user ID is in the 'login' field with a 'uuid' key
                user_id = user.get('login', {}).get('uuid', '')
                if not user_id or user_id in seen_ids:
                    logger.debug(f"User ID missing or duplicate: {user_id}")
                    continue
                
                # Validate email
                email = user.get('email', '')
                if not self.is_valid_email(email):
                    continue
                
                #Add user to transformed list
                transformed.append({
                    'id': user_id,
                    'name': self.normalize_name(user),
                    'email': email,
                    'full_address': self.normalize_address(user)
                })

                seen_ids.add(user_id)
            
            except Exception as e:
                logger.error(f"Error transforming user: {e}")
                continue

        logger.info(f"Transformed {len(transformed)} users successfully")
        return transformed