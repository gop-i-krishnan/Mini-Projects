🔗 Pokémon API Connector (Python)
This is a simple Python script that connects to the PokeAPI to retrieve information about a Pokémon using its name. It demonstrates basic use of the requests module to handle API calls.

📦 Requirements
Python 3.x

requests library

Install requests with:

bash
Copy
Edit
pip install requests
🧾 How It Works
The script sends a GET request to the PokeAPI using a Pokémon's name, then prints the Pokémon's:

Name

Weight

ID

It also handles basic HTTP errors like 404 (not found).

▶️ Usage
Save the script as API_Connect_Program.py.

Run the file using:

bash
Copy
Edit
python API_Connect_Program.py
