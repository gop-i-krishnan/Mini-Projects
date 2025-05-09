

# 📡 API Connect Program — Pokémon Info Fetcher

This Python script demonstrates how to connect to a public API using the `requests` library. It fetches and displays data for a given Pokémon from the [PokeAPI](https://pokeapi.co/).

---

## 🧠 Features

* Connects to the PokeAPI endpoint
* Fetches:

  * Pokémon **name**
  * Pokémon **weight**
  * Pokémon **ID**
* Handles HTTP errors like 404 (Not Found)

---

## 📂 File Structure

```
API_Connect/
├── API_Connect_Program.py  # Main Python script
└── README.md               # Project documentation
```

---

## 📦 Requirements

* Python 3.x
* `requests` library

Install dependencies using pip:

```bash
pip install requests
```

---

## ▶️ How to Run

1. Navigate to the project directory in your terminal.
2. Run the script:

```bash
python API_Connect_Program.py
```

---

## 🔍 Example Output

```text
pikachu
60
25
```

---

## 📜 Code Overview

```python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print('Page not found error')
    else:
        print(f'Failed to retrieve data {response.status_code}')

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info['name']}")
    print(f"{pokemon_info['weight']}")
    print(f"{pokemon_info['id']}")
```

---

## 🌐 API Reference

* Endpoint: `https://pokeapi.co/api/v2/pokemon/{name}`

---

## 📄 License

This project is provided for educational and learning purposes.

---

