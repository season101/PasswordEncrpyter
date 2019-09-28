print("Welcome to the program where we will encrpypt your passowrd in image for you.")

print()

print("Press any key to continue...")
input()

print()
print()

masterKey = ("Enter a key that you want to use throughout your lifetime: ")
imageName = input("Enter the image name you want to put password to: ")
outputName = input("Enter the name for your output image: ")


imageName+= ".jpg"


from cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography(masterKey)
'''
# Save the encrypted file inside the image
crypto_steganography.hide(imagename, 'Encrypted1.png', 'We will rock on')

print("Successfully Encrypted")

'''
secret = crypto_steganography.retrieve('Encrypted1.png')

print(secret)
# My secret message
