# image-qr_generator
Image Upload & QR Code Generator
This project allows you to upload an image to an external hosting service (from https://api.imgbb.com) and automatically generate a QR code linking to the uploaded image.

Features:
1. Uploads local image files to imgBB using their API
2. Generates and displays a QR code linking to the hosted image
3. Dynamic file naming with timestamps
4. All configuration is customizable via params.txt

Requirements:
1. Python 3.7+
2. Installed libraries:
  pip install requests qrcode[pil] pillow

Usage:
1. Prepare your params.txt file:

  - api_key=YOUR_IMGBB_API_KEY
  - image_path=path/to/your/image.jpg
  - qr_output_dir=path/to/output/folder
  - expiration=None  # or a number like 3600 (seconds)

2. Run the script:
  - python image-qr.py path/to/params.txt
  - This will:
      1. Upload the image to imgBB
      2. Print the generated image URL
      3. Save and open a QR code pointing to that URL
   
Notes:
1. Re-uploading the exact same image may return the same URL (imgBB deduplication).
2. You can ensure unique uploads by modifying the image slightly before upload (e.g., watermark, timestamp).
3. The QR code is resized to 400x400 for easier scanning.
