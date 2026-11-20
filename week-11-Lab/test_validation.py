from validation import get_positive_float

def main():
    price = get_positive_float("Enter a positive price: ")
    print(f"Valid price: {price}")


if __name__ == "__main__":
    main()