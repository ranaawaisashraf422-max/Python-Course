def http_status(status):
    match status:
        case 200:
            return "Hmmm"
        case 400:
            return "OK"
        case 600:
            return "Not Found"
        case 900:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
print(http_status(200))
print(http_status(400))
print(http_status(600))
print(http_status(900))
print(http_status(678787))