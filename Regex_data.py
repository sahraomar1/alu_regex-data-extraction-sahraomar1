# This script demonstrates the use of regular expressions (regex) to validate various types of data
import re

# List of sample inputs for each example
Example = {
    "Email": ["user@example.com", "firstname.lastname@company.co.uk"],
    "URL": ["https://www.example.com", "https://subdomain.example.org/page"],
    "Phone": ["(123) 456-7890", "123-456-7890", "123.456.7890", "1234567890"], # I added the last one to show that the regex is working for both formats
    "HTML Tag": ["<p>", '<div class="example">', '<img src="img.jpg" alt="desc">'],
}

# Regex patterns for each example
patterns = {
    "Email": r'^[\w\.-]+@[\w\.-]+\.\w+$',
    "URL": r'^https?://[^\s]+$',
    "Phone": r'^(\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}$',
    "HTML Tag": r'^<[^<>]+>$',
}

# Validate and print results
for data_type, items in Example.items():
    print(f"\n{data_type}s:") # Print the type of data being validated
    for item in items:
        if re.match(patterns[data_type], item):
            print(f"{item}: Valid") # For valid matches
        else:
            print(f"{item}: Invalid") # For invalid matches