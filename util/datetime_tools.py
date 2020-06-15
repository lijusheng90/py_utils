from datetime import datetime, timedelta


def is_valid_date(string, date_format="%Y-%m-%d"):
    try:
        datetime.strptime(string, date_format)
    except:
        return False
    return True


def check_input_datetime_scope(self, expos_date_scope):
    if not isinstance(expos_date_scope, list) or len(expos_date_scope) != 2 \
            or not is_valid_date(expos_date_scope[0], "%Y-%m-%d %H:%M:%S") \
            or not is_valid_date(expos_date_scope[1], "%Y-%m-%d %H:%M:%S"):
        return False
    return True
