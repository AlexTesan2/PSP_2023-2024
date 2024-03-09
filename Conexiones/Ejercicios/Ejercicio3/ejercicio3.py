import requests

def get_country_by_ip(ip_address):
    api_url = f"http://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(api_url)
        data = response.json()

        country = data.get('country')
        return country

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    ip_address = input("Enter the IP address: ")

    country = get_country_by_ip(ip_address)

    if country:
        print(f"The IP address {ip_address} is likely located in {country}.")
    else:
        print(f"Unable to determine the country for {ip_address}.")

if __name__ == "__main__":
    main()
