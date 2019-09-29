from cryptosteganography import CryptoSteganography
masterKey=input()
crypto_steganography = CryptoSteganography(masterKey)
secret = crypto_steganography.retrieve("Ren.png")
print(secret)
input()
