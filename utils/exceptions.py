class APIBaseException(Exception):
    """Base class for other exceptions"""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class UserNotFound(APIBaseException):
    """No data has found for the given filters"""
    def __init__(self, username):
        self.code = 401
        self.username = username
        super().__init__("Username {} not Found. Please Register first.".format(self.username), self.code)


class UserAlreadyPresent(APIBaseException):
    """No data has found for the given filters"""
    def __init__(self, username):
        self.code = 401
        self.username = username
        super().__init__("Username {} is already present. Please try another username.".format(self.username), self.code)


class CoachNotFound(APIBaseException):
    """No data has found for the given filters"""
    def __init__(self, train_id, coach_num, coach_type=""):
        self.code = 401
        self.train_id = train_id
        self.coach_num = coach_num
        self.coach_type = coach_type
        super().__init__("Coach {} {} is does not exist for train-id {}".format(self.coach_num, self.coach_type, self.train_id), self.code)


class CoachAlreadyPresent(APIBaseException):
    """No data has found for the given filters"""
    def __init__(self, train_id, coach_num, coach_type=""):
        self.code = 401
        self.train_id = train_id
        self.coach_num = coach_num
        self.coach_type = coach_type
        super().__init__("Coach {} {} is already present for train-id {}".format(self.coach_num, self.coach_type, self.train_id), self.code)
