import faker
from random import randint

NAMES_NUMBER = 10
EMAILS_NUMBER = NAMES_NUMBER
STATUS_NUMBER = 3
TITLES_NUMBER = NAMES_NUMBER
DESCRIPTIONS_NUMBER = NAMES_NUMBER

def generate_fake_data_users(names_number, emails_number):

    fake_names = []
    fake_emails = []
    
    fake_data = faker.Faker()

    for _ in range(names_number):
        fake_names.append(fake_data.name())

    for _ in range(emails_number):
        fake_emails.append(fake_data.email())

    return fake_names, fake_emails

names, emails = generate_fake_data_users(NAMES_NUMBER, EMAILS_NUMBER)

def generate_fake_data_tasks(title_number, description_number):
    fake_titles = []
    fake_descriptions = []

    fake_data = faker.Faker()

    for _ in range(title_number):
        fake_titles.append(fake_data.catch_phrase())

    for _ in range(description_number):
        fake_descriptions.append(fake_data.text())

    return fake_titles, fake_descriptions

titles, descriptions = generate_fake_data_tasks(TITLES_NUMBER, DESCRIPTIONS_NUMBER)

def prepare_data_users(names, emails):

    for_users = []
    for name in names:
        for_users.append((name, emails.pop(0)))

    return for_users

def prepare_data_tasks(titles, descriptions):
    for_tasks = []
    for task in titles:
        for_tasks.append((task, descriptions.pop(0), randint(1, STATUS_NUMBER), randint(1, NAMES_NUMBER)))
    
    return for_tasks

user_data = prepare_data_users(*generate_fake_data_users(NAMES_NUMBER, EMAILS_NUMBER))
task_data = prepare_data_tasks(*generate_fake_data_tasks(TITLES_NUMBER, DESCRIPTIONS_NUMBER))



