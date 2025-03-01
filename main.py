import pickle
import pandas as pd
from neurion_sanctum.crypt import decrypt_file
from neurion_sanctum.store.huggingface import download_all_encrypted_files, upload_to_huggingface_with_token
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from neurion_sanctum.task.task import Task

MODEL_PATH = "saved_model.pkl"  # Where model will be stored
VECTORIZER_PATH = "saved_vectorizer.pkl"  # Where vectorizer will be stored


def train_model(key: str):
    """
    Function to train a sentiment analysis model using a decrypted dataset.
    This function runs in the background after being triggered by the `/train` endpoint.
    """
    try:
        print("Training started...")

        # Step 1: Download the encrypted dataset
        dataset_url = 'https://huggingface.co/datasets/ryonzhang36/neurion-sanctum-example-dataset'
        download_all_encrypted_files(dataset_url, '.')

        # Step 2: Decrypt the dataset
        decrypt_file(key, 'encrypted_dataset.json.enc', 'decrypted_dataset.json')

        # Step 3: Load the dataset
        df = pd.read_json('decrypted_dataset.json', lines=True)

        if "text" not in df.columns or "label" not in df.columns:
            raise ValueError("Dataset must have 'text' and 'label' columns.")

        X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

        vectorizer = TfidfVectorizer(stop_words="english")
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)

        model = LogisticRegression(max_iter=1000)
        model.fit(X_train_vec, y_train)

        y_pred = model.predict(X_test_vec)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"Training complete! Model Accuracy: {accuracy:.4f}")

        # Save the trained model and vectorizer
        with open(MODEL_PATH, "wb") as model_file:
            pickle.dump(model, model_file)
        with open(VECTORIZER_PATH, "wb") as vectorizer_file:
            pickle.dump(vectorizer, vectorizer_file)

        print(f"Model saved to '{MODEL_PATH}' and vectorizer to '{VECTORIZER_PATH}'")

    except Exception as e:
        print(f"Training failed: {str(e)}")


def upload(data: dict):
    """
    Function to upload the trained model or any related files to Cloud storage.
    This function runs in the background after being triggered by the `/upload` endpoint.
    :param data:
    :return:
    """
    upload_to_huggingface_with_token([MODEL_PATH,VECTORIZER_PATH], 'neurion-sanctum-example-model', data['token'])



if __name__ == "__main__":
    Task.create_training_task(train_model,upload).start()