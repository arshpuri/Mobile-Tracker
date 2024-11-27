import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        time_zoneinfo = timezone.time_zones_for_number(parsed_number)
        region_info = geocoder.description_for_number(parsed_number, "en")
        carrier_info = carrier.name_for_number(parsed_number, "en")

        print(f"Phone Number: {phone_number}")
        print(f"Timezone: {time_zoneinfo}")
        print(f"Country: {region_info}")
        print(f"Carrier: {carrier_info}")

    except phonenumbers.NumberParseException as e:
        print(f"Error parsing phone number: {e}")

if __name__ == "__main__":
    # Example phone numbers: replace these with the desired phone numbers
    phone_numbers = input("Enter phone number with country code: ")

    for phone_number in phone_numbers:
        get_phone_info(phone_number)
        print("=" * 30)


'''
In this example, the phonenumbers module is used to parse the input phone number and obtain information such as the country, region, and carrier.
 The geocoder module provides information about the geographical region associated with the phone number, and the carrier module provides information about the carrier.

Note that the phonenumbers module is quite flexible and can handle various phone number formats.
 It is important to ensure that the provided phone number is correctly formatted, including the country code.'''
'''
'''import phonenumbers
from phonenumbers import timezone, geocoder, carrier

import opencage
from opencage.geocoder import OpenCageGeocode

key = "9bc4311342a2457dbbf4e82d40b49462"

try:

    number = input("Enter your Number with country code( for example for India +91): ")
    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    provider = carrier.name_for_number(phone, "en")
    location = geocoder.description_for_number(phone, "en")

    geo_code = OpenCageGeocode(key)
    query = str(location)
    results = geo_code.geocode(query)

    lat = results[0]['geometry']['lat']
    long = results[0]['geometry']['long']

    print(phone)
    print(time)
    print(provider)
    print(location)
    print(lat, long)



except:

    print(
        ''' 
    There is an error amongst the following

    i) Error in the digits of the phone number

    ii) Error in the country code

    iii) Or the  Phone number does not exist
    '''
    )


