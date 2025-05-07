import requests
import qrcode
from PIL import Image
import os
import time

def load_params(file_path="params.txt"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    
    params = {}
    with open(file_path, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                params[key.strip()] = value.strip()
    return params

def upload_to_imgbb(image_path, api_key, expiration=None):
    params = {"key": api_key}
    if expiration and expiration.lower() != "none":
        params["expiration"] = expiration

    with open(image_path, 'rb') as file:
        response = requests.post(
            "https://api.imgbb.com/1/upload",
            params=params,
            files={"image": file}
        )
    response.raise_for_status()
    return response.json()["data"]["url"]

def generate_and_show_qr(url, qr_path="qr_code.png"):
    qr = qrcode.make(url)
    qr.save(qr_path)
    print(f"QR code saved to: {qr_path}")
    
    img = Image.open(qr_path)
    img = img.resize((400, 400))
    img.show()

def main(params_path):
    try:
        config = load_params(params_path)

        api_key = config["api_key"]
        image_path = config["image_path"]
        qr_output_dir = config["qr_output_dir"]
        expiration_seconds = config.get("expiration", None)

        timestamp = str(int(time.time()))
        qr_output_path = os.path.join(qr_output_dir, f"qr_image_{timestamp}.png")

        uploaded_url = upload_to_imgbb(image_path, api_key, expiration_seconds)
        print("Image URL:", uploaded_url)
        generate_and_show_qr(uploaded_url, qr_output_path)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main("C:/Users/User/Desktop/image-qr/params.txt") # This is the path to your params.txt file
