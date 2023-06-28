import ipfshttpclient

def upload_image(image_path):
    client = ipfshttpclient.connect()  # برقراری ارتباط با گره IPFS محلی

    try:
        res = client.add(image_path)  # ارسال عکس به IPFS
        image_hash = res['Hash']  # دریافت هش عکس بارگذاری شده
        return image_hash
    except Exception as e:
        print(f"Error uploading image: {str(e)}")
        return None

# مسیر فایل عکس را وارد کنید
image_path = 'path_to_your_image.jpg'

image_hash = upload_image(image_path)
if image_hash:
    print("Image uploaded successfully.")
    print("Image Hash:", image_hash)
