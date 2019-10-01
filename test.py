print("Welcome to the program where we will encrpypt your passowrd in image for you.")

print()

print("Press any key to continue...")
input()

print()
print()

masterKey = input("Enter a key that you want to use throughout your lifetime: ")
imageName = input("Enter the image name you want to put password to: ")
outputName = input("Enter the name for your output image: ")
print()

imageName+= ".jpg"
outputName+= ".png"

from cryptosteganography import CryptoSteganography

crypto_steganography = CryptoSteganography(masterKey)

# Save the encrypted file inside the image
passcode = input("Enter your secret passcode: ")
crypto_steganography.hide(imageName,outputName,passcode)

print("Successfully Encrypted...")
