from cryptography.hazmat.primitives.ciphers.aead import (
    AESGCM,
)


def encrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    # A implémenter en utilisant la class AESGCM

    Classe = AESGCM(key)
    return Classe.encrypt(nonce, msg, None)


def decrypt(msg: bytes, key: bytes, nonce: bytes) -> bytes:
    # A implémenter en utilisant la class AESGCM

    Classe = AESGCM(key)
    return Classe.decrypt(nonce, msg, None)
