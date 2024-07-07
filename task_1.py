from datetime import datetime, date


def transform_str_to_date(date_str:str)->date:
    return datetime.strptime(date_str, '%Y-%m-%d').date()

def get_days_from_today(date_str: str)->int:
    try:        
        transform_to_date = transform_str_to_date(date_str)
        current_date = datetime.today().date()
        return (current_date - transform_to_date).days
    except ValueError:
        raise ValueError('Invalid date format. Enter the date in the following format YYYY-MM-DD')



print(get_days_from_today('2021-10-09'))

print(get_days_from_today('09-10-2021'))
