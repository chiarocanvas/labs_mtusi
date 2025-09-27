import fire

def describe_person(name: str, age: int = 30):
    """Описывает человека по имени и возрасту"""
    print(f"Человек по имени {name}, возраст: {age} лет")

def is_prime(number: int) -> bool:
    """Проверяет, является ли число простым"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    fire.Fire({
        'task1': describe_person,
        'is_prime': is_prime
    })