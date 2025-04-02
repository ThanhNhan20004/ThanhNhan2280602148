import base64

def main():
    input_string = input("Nhập thông tin cần mã hoá: ")

    encoded_bytes = base64.b64encode
    encoded_string = encoded_bytes.decode("utf-8")

    with open("data.txt", "w") as file:
        file.write(encode_string)

    print("Đã mã hoá và ghi vào tệp data.txt")

if_name_ == "__main__":
    main()