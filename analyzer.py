import re
from collections import Counter

with open("urls.txt", "r") as file:
    urls = [line.strip() for line in file]

product_pattern = r"/product/"
category_pattern = r"/category/"
login_pattern = r"/login"

product_count = 0
category_count = 0
login_count = 0

for url in urls:
    if re.search(product_pattern, url):
        product_count += 1

    if re.search(category_pattern, url):
        category_count += 1

    if re.search(login_pattern, url):
        login_count += 1

duplicates = [url for url, count in Counter(urls).items() if count > 1]

report = f"""
Total URLs: {len(urls)}

Product URLs: {product_count}
Category URLs: {category_count}
Login URLs: {login_count}

Duplicate URLs:
"""

for d in duplicates:
    report += f"{d}\n"

print(report)

with open("report.txt", "w") as f:
    f.write(report)
