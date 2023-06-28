import ipfshttpclient

def download_image(image_hash):
    client = ipfshttpclient.connect()  # برقراری ارتباط با گره IPFS محلی

    try:
        client.get(image_hash)  # دریافت عکس با استفاده از هش عکس
        print("Image downloaded successfully.")
    except Exception as e:
        print(f"Error downloading image: {str(e)}")

# هش عکس را که از ارسال کننده دریافت کرده‌اید، وارد کنید
image_hash = 'QmWc3pwe6dZum4E8wpgiXJXDV6qwVCHuXgAep9MNLJKC4i'

download_image(image_hash)
