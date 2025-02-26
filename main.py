import dotenv
import requests
from neurion_ganglion.custom_types.capacity import Capacity
from neurion_ganglion.ion.ion import Ion, ion_handler
from neurionpy.synapse.config import NetworkConfig
from pydantic import BaseModel

dotenv.load_dotenv()

if __name__ == "__main__":
    result=Ion.at("ion17xgmzvxar06w7ukv8wpwgq9fnf9zeekdp8gcrw").call({'score':3,'result':33})
    print(result)