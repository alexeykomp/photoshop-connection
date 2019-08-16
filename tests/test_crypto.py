from photoshop.crypto import EncryptDecrypt

PASSWORD = b'lei6ooH6ieyeenga'

DECRYPTED = (
    b'\x00\x00\x00\x01\x00\x00\x00\x0c'
    b'\x00\x00\x00\x02\x73\x74\x72\x69'
    b'\x6e\x67\x49\x44\x54\x6f\x54\x79'
    b'\x70\x65\x49\x44\x28\x27\x73\x65'
    b'\x6c\x65\x63\x74\x69\x6f\x6e\x4c'
    b'\x61\x62\x4c\x61\x73\x73\x6f\x54'
    b'\x6f\x6f\x6c\x27\x29\x0a'
)

ENCRYPTED = (
    b'\x6a\xb9\xe1\x94\xe2\x08\xca\xd0'
    b'\x8e\x5b\x72\x0b\xbd\x9d\x0c\x15'
    b'\x46\x10\x6d\x87\xa7\x14\xc7\x45'
    b'\xd6\xfb\x6f\xab\x64\x28\x93\xc9'
    b'\xa3\xd3\x6d\x8b\x25\x14\xe6\x8e'
    b'\x58\x8c\x59\xc7\xff\x47\x57\xcb'
    b'\x0a\x52\xd8\x83\xe9\x04\x5e\xf1'
)


def test_encrypt_decrypt():
    f = EncryptDecrypt(PASSWORD)
    assert f.encrypt(DECRYPTED) == ENCRYPTED
    assert f.decrypt(ENCRYPTED) == DECRYPTED
