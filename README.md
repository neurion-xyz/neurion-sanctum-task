# **Neurion Sanctum Task**

## **Overview**
This library provides a secure execution environment for processing **dataset usage requests** using **Trusted Execution Environments (TEE)**. It allows dataset owners to **securely train models** while ensuring **zero leakage of encryption keys** and **uploading results** to cloud storage.

Users only need to provide:
- A **training function** to process the dataset securely inside the enclave.
- An **upload function** to store the results.

## **Installation**
Before using the library, install it using:
```sh
pip install neurion-sanctum
```

## **Usage**
To create a secure task, define **two functions**:

### 1. Training Function (`train_model`)
This function is triggered directly by the dataset owner and runs securely in the enclave to prevent key leakage.**

```python
def train_model(key: str):
    """
    Secure training function that processes an encrypted dataset inside the enclave.
    The dataset owner provides the key, which is never exposed outside the enclave.
    """
    pass  # Implement training logic here
```

### 2. Upload Function (`upload`)
This function uploads the results to the cloud storage, using credentials provided by the dataset requester.**

```python
def upload(data: dict):
    """
    Handles secure upload of the trained model and results.
    """
    pass  # Implement upload logic here
```

### **3. Start the Task**
Once the functions are defined, initiate the task:

```python
from neurion_sanctum.task.task import Task

Task.create_training_task(train_model, upload).start()
```

## **Security**
- **Enclave Execution**: The `train_model` function executes in a **TEE**, ensuring that the encryption key remains confidential.
- **Secure Upload**: The `upload` function allows dataset requesters to store results without exposing credentials.

## **License**
This project is licensed under the **MIT License**.

