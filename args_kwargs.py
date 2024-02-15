def student(name, age, *details, **additonal_details):
    print(f"The name of the student is {name}, age is {age}")
    if details:
        print("Additional Details:")
        for detail in details:
            print(f"- {detail}")

    if additonal_details:
        for k, v in additonal_details.items():
            print(f"{k}: {v}")


student("Lawrence", 13, "tuli na", "Pogi", "Cute", fave_color="red", fave_food="Sinigang")


def teacher(name, age, *anything, **additional_info):
    vals = {
        'name': name,
        'age': age,
    }

    vals.update(additional_info)

    print('vals>', vals)

    if anything:
        print("Anything:")
        for a in anything:
            print("   ", a)


teacher("Rona", '17', 'anything in Rona', 'anything version 2', 'anything version 3',
        address="Rizal")

