import phonenumbers
from phonenumbers import geocoder
number=input("enter any number to check location:")
numberch=phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(numberch,"en"))
from phonenumbers import carrier
sunny=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(sunny,"en"))
