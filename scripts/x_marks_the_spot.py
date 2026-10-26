"""Ejemplo reconstruido desde X Marks the Spot (bitácora, p. 18)."""
import re

CIPHERTEXT = bytes.fromhex(
    "02362b2964302c2164372c25202b3337642b22641734212730362164"
    "1021272c2a2b282b233d7e6420212520222527213f3c2b361b751b"
    "263d30771b70301b701b3075297739"
)

def solve():
    matches = []
    for key in range(256):
        plain = bytes(value ^ key for value in CIPHERTEXT)
        flag = re.search(rb"deadface\{[^}]+\}", plain)
        if flag:
            if bytes(value ^ key for value in plain) != CIPHERTEXT:
                raise ValueError("La comprobación inversa falló")
            matches.append((key, plain.decode("ascii"), flag.group().decode("ascii")))
    if len(matches) != 1:
        raise ValueError(f"Se esperaba un resultado único; se obtuvieron {len(matches)}")
    return matches[0]

if __name__ == "__main__":
    key, message, flag = solve()
    print(f"Clave: 0x{key:02x}")
    print(message)
    print(flag)

