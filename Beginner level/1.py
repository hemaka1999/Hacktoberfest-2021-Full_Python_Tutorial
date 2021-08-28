import Crypto


key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)
