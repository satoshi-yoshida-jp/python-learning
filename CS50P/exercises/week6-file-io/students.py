import csv

name = input("Whats your name? ")
country = input("Whats your country? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "country"])
    writer.writerow({"name": name, "country": country})
