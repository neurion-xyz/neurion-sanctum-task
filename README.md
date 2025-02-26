# Calling an Ion using Neurion Ganglion

## Overview
This guide demonstrates how to call a registered Ion within the Neurion Ganglion ecosystem. The Ion is queried remotely by its unique address, and the request payload is sent for processing.

## Prerequisites
Ensure you have the following installed and set up:
- Python 3.8+
- `neurion-ganglion` package installed (`pip install neurion-ganglion`)
- A registered Ion address
- `.env` file with necessary configurations (optional but recommended)

## Installation

```sh
pip install neurion-ganglion
```

## Usage

### 1. Define the Calling Script
Create a `main.py` file and add the following content:

```python
import dotenv
import requests
from neurion_ganglion.ion.ion import Ion

dotenv.load_dotenv()

if __name__ == "__main__":
    result = Ion.at("ion17xgmzvxar06w7ukv8wpwgq9fnf9zeekdp8gcrw").call({'score': 3, 'result': 33})
    print(result)
```

### 2. Running the Script
Run the script using:

```sh
python main.py
```

This will send a request to the Ion and print the response.

## License
This project is licensed under the MIT License. 
