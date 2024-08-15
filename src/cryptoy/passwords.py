import hashlib
import os
from random import (
    Random,
)

import names


def hash_password(password: str) -> str:
    return hashlib.sha3_256(password.encode()).hexdigest()


def random_salt() -> str:
    return bytes.hex(os.urandom(32))


def generate_users_and_password_hashes(
    passwords: list[str], count: int = 32
) -> dict[str, str]:
    rng = Random()  # noqa: S311

    users_and_password_hashes = {
        names.get_full_name(): hash_password(rng.choice(passwords))
        for _i in range(count)
    }
    return users_and_password_hashes


def attack(passwords: list[str], passwords_database: dict[str, str]) -> dict[str, str]:
    users_and_passwords = {}

    # A implémenter
    # Doit calculer le mots de passe de chaque utilisateur grace à une attaque par dictionnaire

    hashed_password = {}
    for password in passwords:
        hash = hash_password(password)
        hashed_password[password] = hash
    for i, (user, hash1) in enumerate(passwords_database.items()):
        for i, (password, hash2) in enumerate(hashed_password.items()):
            if hash1 == hash2:
                users_and_passwords[user] = password
    return users_and_passwords


def fix(
    passwords: list[str], passwords_database: dict[str, str]
) -> dict[str, dict[str, str]]:
    users_and_passwords = attack(passwords, passwords_database)

    users_and_salt = {}
    new_database = {}

    # A implémenter
    # Doit calculer une nouvelle base de donnée ou chaque élement est un dictionnaire de la forme:
    # {
    #     "password_hash": H,
    #     "password_salt": S,
    # }
    # tel que H = hash_password(S + password)

    for i, (user, password) in enumerate(users_and_passwords.items()):
        salt = random_salt()
        users_and_salt = {
            "password_hash": hash_password(password + salt),
            "password_salt": salt,
        }
        new_database[user] = users_and_salt

    return new_database


def authenticate(
    user: str, password: str, new_database: dict[str, dict[str, str]]
) -> bool:
    # Doit renvoyer True si l'utilisateur a envoyé le bon password, False sinon
    arr = new_database[user]
    pass_hash = hash_password(password + arr["password_salt"])
    if arr["password_hash"] == pass_hash:
        return True
    else:
        return False
