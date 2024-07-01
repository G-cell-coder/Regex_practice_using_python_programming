def is_decimal(num):
    import re 
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)

print(is_decimal('123.11'))
print(is_decimal('12.1212'))
print(is_decimal('100079012'))
print(is_decimal('e29.476'))
