from enum import Enum

class Role(str, Enum):
    student = "student"
    introductor = "introductor"
    admin = "admin"

