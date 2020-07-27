from datetime import datetime, timedelta


def is_valid_date(string, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(string, date_format)
    except ValueError:
        return False
    return True


def check_input_datetime_scope(self, expos_date_scope):
    if not isinstance(expos_date_scope, list) or len(expos_date_scope) != 2 \
            or not is_valid_date(expos_date_scope[0], "%Y-%m-%d %H:%M:%S") \
            or not is_valid_date(expos_date_scope[1], "%Y-%m-%d %H:%M:%S"):
        return False
    return True


def calculate_age(date_of_birth, date_format="%Y-%m-%d"):
    today = datetime.today()
    # 故意不捕获异常，调用方需要处理，防止掩盖错误
    date_of_birth = datetime.strptime(date_of_birth, date_format)
    try:
        birthday = date_of_birth.replace(year=today.year)
    except ValueError:
        birthday = date_of_birth.replace(year=today.year, day=date_of_birth.day-1)
    age = today.year - date_of_birth.year
    if birthday > today:
        age -= 1
    return max(1, age)


def string_to_datetime(date_s, date_format="%Y-%m-%d"):
    return datetime.strptime(date_s, date_format)


if __name__ == "__main__":
    print(is_valid_date("1999-01-02"))
    print(is_valid_date("cccc-01-02"))
    print(string_to_datetime("1999-01-02"))
