from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_user_birthdays = []

    for user in users: 
        user_birthday = user['birthday']
        formatted_birthday_in_date = datetime.strptime(user_birthday, '%Y.%m.%d').date()

        birthday_this_year = formatted_birthday_in_date.replace(year = today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days

        if 0<= days_until_birthday  <=7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days = 2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days = 1)

            upcoming_user_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_user_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Harry Potter", "birthday": "1990.07.13"},
    {"name": "Jude Bellingham", "birthday": "1990.07.08"},
    {"name": "Jo Brown", "birthday": "1990.07.14"}
]

print(get_upcoming_birthdays(users))