"""Ejemplo reconstruido desde la ficha Hail Caesar (bitácora, p. 16)."""
import codecs

MESSAGE = "Zl qbt'f anzr vf Srgpu"

def solve():
    plain = codecs.decode(MESSAGE, "rot_13")
    if codecs.encode(plain, "rot_13") != MESSAGE:
        raise ValueError("La comprobación inversa falló")
    return plain, "deadface{" + plain.rsplit(" ", 1)[-1] + "}"

if __name__ == "__main__":
    message, flag = solve()
    print(message)
    print(flag)

