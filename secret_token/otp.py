import pyotp
import base64


def verify_result(secret_key, verifycode):
    result = pyotp.TOTP(secret_key).verify(verifycode)
    return result if result is True else False


def generate_uri(secret_key, provisioning='test/test'):
    # generate uri ,can use to generate QR code for "google authenticator"
    return pyotp.totp.TOTP(secret_key).provisioning_uri(provisioning)


def generate_secret(raw_secret):
    return base64.b32encode(raw_secret.encode("utf-8"))


def generate_verify_code(secret):
    return pyotp.TOTP(secret).now()


if __name__ == "__main__":
    # PyOTP is a Python library for generating and verifying one-time passwords.
    # https://github.com/idorax/pyotp
    raw_secret = "PJy1EWA9lK"
    secret = generate_secret(raw_secret)
    print(generate_uri(secret))
    verify_code = generate_verify_code(secret)
    print(verify_code)
    print(verify_result(secret, verify_code))
