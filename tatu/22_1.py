from collections import Counter

def find_and_print_duplicates(vector):
    # Elementlarni sanash
    counter = Counter(vector)

    # Bir xil qiymatdagi elementlarni aniqlash va ekranga chiqarish
    print("Bir xil qiymatdagi elementlar:")
    for element, count in counter.items():
        if count > 1:
            print(f"{element}: {count} marta")

# Satrli tipdagi vektor
vector = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Funksiyani chaqirish
find_and_print_duplicates(vector)
