OPENING_BALANCE = 10000
MAX_AMOUNT = 100000


def validate_transaction(transaction_type, amount, balance):

    
    if transaction_type not in ["Deposit", "Withdraw"]:
        return False, "Unknown type"

    
    if amount <= 0:
        return False, "Amount must be positive"

    
    if amount > MAX_AMOUNT:
        return False, "Amount exceeds limit of 100000"

    
    if transaction_type == "Withdraw" and amount > balance:
        return False, "Insufficient balance"

    return True, "Valid"



def main():

    balance = OPENING_BALANCE

    valid_count = 0
    invalid_count = 0

    valid_transactions = []

    try:
        
        with open("transactions.txt", "r") as file:

            transactions = file.readlines()

        
        for line_number, line in enumerate(transactions, start=1):

            line = line.strip()

            
            if not line:
                continue

            try:
                
                transaction_type, amount = line.split(",")

                amount = float(amount)

                
                is_valid, reason = validate_transaction(
                    transaction_type, amount, balance
                )

                if is_valid:

                    # Update balance
                    if transaction_type == "Deposit":
                        balance += amount

                    elif transaction_type == "Withdraw":
                        balance -= amount

                    valid_count += 1

                    valid_transactions.append(line)

                    print(
                        f"Line {line_number}: Valid | "
                        f"Balance: {balance:g}"
                    )

                else:
                    invalid_count += 1

                    print(
                        f"Line {line_number}: Invalid - {reason}"
                    )

            except ValueError:
                invalid_count += 1
                print(
                    f"Line {line_number}: Invalid - "
                    "Amount must be a number"
                )

            except Exception as error:
                invalid_count += 1
                print(f"Line {line_number}: Invalid - {error}")

        
        with open("valid_transactions.txt", "w") as file:

            for transaction in valid_transactions:
                file.write(transaction + "\n")

        
        print("\n========== FINAL SUMMARY ==========")

        print("Valid transactions:", valid_count)
        print("Invalid transactions:", invalid_count)
        print("Final balance:", balance)

        print("\nValid transactions saved successfully!")

    except FileNotFoundError:
        print("Error: transactions.txt file not found!")

    except Exception as error:
        print("An unexpected error occurred:", error)



if __name__ == "__main__":
    main()
