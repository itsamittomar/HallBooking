import json
from controller.controller import app

PORT = 8085

def initialize_database():
    """
    Initializes and pre-populates bookings in json file
    File name - database/booking.json
    """
    with open("database/booking.txt", "w") as outfile:
        print(outfile,"nkjndkjfd")
        bookings = [{"id": "2546543", "hallName": "A", "capacity": 50, "startDate": "2021-06-27 15:00:00",
                     "endDate": "2021-06-27 16:00:00"},
                    {"id": "2546541", "hallName": "A", "capacity": 50, "startDate": "2021-06-27 16:30:00",
                     "endDate": "2021-06-27 18:00:00"},
                    {"id": "2546531", "hallName": "B", "capacity": 100, "startDate": "2021-06-27 15:00:00",
                     "endDate": "2021-06-27 16:00:00"},
                    {"id": "2546521", "hallName": "C", "capacity": 200, "startDate": "2021-06-27 15:00:00",
                     "endDate": "2021-06-27 16:00:00"},
                    {"id": "2546511", "hallName": "D", "capacity": 350, "startDate": "2021-06-27 15:00:00",
                     "endDate": "2021-06-27 16:00:00"}]
        for booking in bookings:
            outfile.write(json.dumps(booking) + "\n")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, threaded=True)
