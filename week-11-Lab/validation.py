def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                raise ValueError("Value must be greater than zero.")

        except ValueError as error:
            print(f"Invalid input: {error}")

        else:
            return value