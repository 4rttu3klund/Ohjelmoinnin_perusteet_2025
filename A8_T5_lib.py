import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"

def hashPassword(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def loadCredentials() -> list[tuple[int, str, str]]:
    credentials = []
    if not os.path.exists(CREDENTIALS_FILE):
        return credentials
    File = open(CREDENTIALS_FILE, "r")
    for line in File:
        line = line.strip()
        if line:
            parts = line.split(";")
            if len(parts) == 3:
                userId = int(parts[0])
                username = parts[1]
                passwordHash = parts[2]
                credentials.append((userId, username, passwordHash))
    return credentials

def saveCredentials(credentials: list[tuple[int, str, str]]) -> None:
    File = open(CREDENTIALS_FILE, "w")
    for userId, username, passwordHash in credentials:
        File.write(f"{userId};{username};{passwordHash}\n")

def registerUser(username: str, password: str) -> None:
    credentials = loadCredentials()
    newId = len(credentials)
    passwordHash = hashPassword(password)
    credentials.append((newId, username, passwordHash))
    saveCredentials(credentials)

def authenticate(username: str, password: str):
    credentials = loadCredentials()
    passwordHash = hashPassword(password)
    for user in credentials:
        if user[1] == username and user[2] == passwordHash:
            return user
    return None