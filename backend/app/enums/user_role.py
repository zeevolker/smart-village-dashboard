from enum import Enum


class UserRole(str, Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN_DESA = "ADMIN_DESA"
    KEPALA_DESA = "KEPALA_DESA"
    OPERATOR = "OPERATOR"
    WARGA = "WARGA"
