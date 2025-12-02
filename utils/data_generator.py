from faker import Faker

faker = Faker()


def random_email():
    return faker.email()


def random_password():
    return faker.password(length=12)


def random_name():
    return faker.name()


def random_word():
    return faker.word()


def random_text():
    return faker.text()
