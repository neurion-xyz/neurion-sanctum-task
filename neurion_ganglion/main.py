from pydantic import BaseModel

from neurion_ganglion.ion.ion import Ion, ion_handler
from neurion_ganglion.types.capacity import Capacity


# Define Input Schema
class MyInputSchema(BaseModel):
    task_id: str
    parameters: int

# Define Output Schema
class MyOutputSchema(BaseModel):
    message: str
    result: float

# Use decorator to attach schemas
@ion_handler(MyInputSchema, MyOutputSchema)
def my_ion_handler(data: MyInputSchema) -> MyOutputSchema:
    """Handles execution logic."""
    return MyOutputSchema(message="Success", result=12)

# Start Ion Server
if __name__ == "__main__":
    description = "My custom Ion server"
    stake = 20000000
    fee_per_thousand_calls = 1
    capacities = [Capacity.SCRAPER, Capacity.AI_AGENT]
    Ion.create_self_hosting_ion(description,stake,fee_per_thousand_calls,capacities,my_ion_handler).start()
    #
    # endpoints = ["http://167.99.69.198:8000"]
    # Ion.create_server_ready_ion(description,stake,fee_per_thousand_calls,capacities,MyInputSchema,MyOutputSchema,endpoints).register_ion()