import cv2
import os

# Function to encrypt the message into the image
def encrypt_message(image, msg):
    d = {chr(i): i for i in range(255)}  # Character to ASCII mapping
    m, n, z = 0, 0, 0

    for char in msg:
        image[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    return image

# Function to decrypt the message from the image
def decrypt_message(image, password, msg):
    c = {i: chr(i) for i in range(255)}  # ASCII to character mapping
    decrypted_message = ""
    n, m, z = 0, 0, 0

    pas = input("Enter passcode for Decryption: ")

    if password == pas:
        for _ in range(len(msg)):
            decrypted_message += c[image[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        print("Decryption message:", decrypted_message)
    else:
        print("Not a valid key")

# Take user input for image file name
image_file = input("Enter the image file name (with extension): ")

# Read the image
img = cv2.imread(image_file)

# Take user input for secret message and password
msg = input("Enter secret message: ")
password = input("Enter password: ")

# Encrypt the message into the image
img_encrypted = encrypt_message(img.copy(), msg)

# Save the encrypted image
cv2.imwrite("Encryptedmsg.jpg", img_encrypted)

# Display the encrypted image
os.system("start Encryptedmsg.jpg")

# Decrypt the message from the encrypted image
decrypt_message(img_encrypted, password, msg)
