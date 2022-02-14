weekdays = {
    "mo": "Montag",
    "di": "Dienstag",
    "mi": "Mittwoch",
    "do": "Donnerstag",
    "fr": "Freitag",
    "sa": "Samstag",
    "so": "Sonntag",
}


while True:
    enteredDay = input("Welcher Tag? (Mo, Di, Mi, Do, Fr, Sa, So): ").lower()
    if enteredDay == "ende":
        print("Programm beendet")
        break

    print(weekdays.get(enteredDay, "Ungültiger Tag"))
    print("-"*20)
