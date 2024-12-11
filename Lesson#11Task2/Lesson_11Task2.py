pets = {}



def get_suffix(age):
    if 11 <= age % 100 <= 19:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"




def create():
    import collections
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1
    pet_name = input('Введите имя питомца: ').strip()
    pet_type = input('Введите вид питомца: ').strip()
    pet_age = int(input('Введите возраст питомца: '))
    owner_name = input('Введите имя владельца: ').strip()
    pets[new_id] = {
        pet_name: {
            'Вид питомца': pet_type,
            'Возраст питомца': pet_age,
            'Имя владельца': owner_name 
            }
        }
    print(f'Питомец с ID {new_id} успешно создан!!')



def read():
    pet_id = int(input('Введите ID питомца: '))
    pet_data = get_pet(pet_id)
    if pet_data:
        for pet_name, details in pet_data.items():
            age_suffix = get_suffix(details["Возраст питомца"])
            print(
                f"Это {details['Вид питомца']} по кличке \"{pet_name}\". "
                f"Возраст питомца: {details['Возраст питомца']} {age_suffix}. "
                f"Имя владельца: {details['Имя владельца']}."
            )
    else:
        print('Питомца с таким ID не найдено')



       




def update():
    pet_id = int(input('Введите ID питомца: '))
    pet_data = get_pet(pet_id)
    if pet_data:
        pet_data = pets[pet_id]
        items_to_update = list(pet_data.items())
        for pet_name, details in items_to_update:
            print(f"Сейчас данные такие: Имя питомца: {pet_name}, {details}")
            new_pet_name = input("Введите новое имя питомца (или оставьте без изменений): ").strip() or pet_name
            new_pet_type = input("Введите новый вид питомца (или оставьте без изменений): ").strip() or details["Вид питомца"]
            new_pet_age = input("Введите новый возраст питомца (или оставьте без изменений): ").strip()
            new_pet_age = int(new_pet_age) if new_pet_age else details["Возраст питомца"]
            new_owner_name = input("Введите новое имя владельца (или оставьте без изменений): ").strip() or details["Имя владельца"]
            if new_pet_name != pet_name:
                del pet_data[pet_name]
            pet_data[new_pet_name] = {
                "Вид питомца": new_pet_type,
                "Возраст питомца": new_pet_age,
                "Имя владельца": new_owner_name
            }
        print("Данные успешно обновлены!")
    else:
        print("Питомца с таким ID не найдено")



def delete():
    pet_id = int(input('Введите ID питомца: '))
    pet_data = get_pet(pet_id)
    if pet_data:
        del pets[pet_id]
        print('Данные питомца успешно удалены!')
    else:
        print('Такого ID не было найдено')


def list_pets():
    if not pets:
        print('Питомцев нет!')
    else:
        print("Список всех питомцев:")
        for pet_id, pet_data in pets.items():
            for pet_name, details in pet_data.items():
                age_suffix = get_suffix(details["Возраст питомца"])
                print(
                    f"ID: {pet_id} | "
                    f"Имя: {pet_name} | "
                    f"Вид: {details['Вид питомца']} | "
                    f"Возраст: {details['Возраст питомца']} {age_suffix} | "
                    f"Владелец: {details['Имя владельца']}"
                )

def get_pet(ID):
    if ID in pets:
        return pets[ID]
    else:
        return False



while True:
    command = input('Введите команду: ').strip().lower()
    if command == 'stop':
        print('Программа завершена!!!')
        break
    elif command == 'create':
        create()

    elif command == 'read':
        read()

    elif command == 'update':
        update()

    elif command == 'delete':
        delete()

    elif command == 'list':
        list_pets()
    else:
        print('Неизвестная комманда')
