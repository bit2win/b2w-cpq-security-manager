class GenericSecurityException(Exception):
    def __init__(
        self,
        status_code,
        code="E-001-GENERAL-SECURITY-MANAGER-ERROR",
        message="Security Manager Exception",
    ):
        self.status_code = status_code
        self.code = status_code if code is None else code
        self.message = message
        self.detail = {"code": self.code, "message": self.message}
        super().__init__(self.message)


class UpdateSecurityException(Exception):
    def __init__(
        self,
        status_code,
        code="E-002-UPDATE-SECURITY-MANAGER-ERROR",
        message="Update Policies Exception",
    ):
        self.status_code = status_code
        self.code = status_code if code is None else code
        self.message = message
        self.detail = {"code": self.code, "message": self.message}
        super().__init__(self.message)
