seat_type = input("Enter the seat type (sleeper/AC/general/luxury): ")

match seat_type:
    case "sleeper":
        print("Sleeper seat")
    case "AC":
        print("AC seat")
    case "general":
        print("General seat")
    case "luxury":
        print("Luxury seat")
    case _:
        print("Invalid seat type")