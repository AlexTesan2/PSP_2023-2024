import whois

def perform_whois_lookup(target):
    try:
        result = whois.whois(target)
        return result
    except whois.parser.PywhoisError as e:
        return f"Error: {e}"

def main():
    target = input("Enter an IP or host address: ")
    whois_result = perform_whois_lookup(target)

    print("\nWHOIS Results:")
    print(whois_result)

if __name__ == "__main__":
    main()
