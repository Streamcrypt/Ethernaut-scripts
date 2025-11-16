tx_origin = input("Input your tx.origin address/the address that appears in the wallet:\nMake sure it start from 0x!: ").strip()
addr = tx_origin.replace("0x" , "")
val_160 = int(addr, 16)
val_16 = val_160 & 0xFFFF
padded_64bit = format(int(val_16), '064b')
modified_bit = '1' + padded_64bit[1:]
num = int(modified_bit, 2)
bytes8_val = num.to_bytes(8)
print("Your gatekeeper key is >>  ", "0x" + bytes8_val.hex())
