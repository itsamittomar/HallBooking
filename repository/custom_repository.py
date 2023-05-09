import json

class Repository:
    """
    Class for database client
    """
    def __init__(self):
        pass

    def fetch_sample_bookings(self):
        """
        Returns random bookings for demo
        param-
            None
        return -
            sample_bookings - list
        """
        sample_bookings = [{"id": "2546543", "hallName": "A", "capacity": 50, "startDate": "2021-06-27 15:00:00",
                     "endDate": "2021-06-27 16:00:00"},
                    {"id": "2546541", "hallName": "B", "capacity": 50, "startDate": "2021-06-27 16:30:00",
                     "endDate": "2021-06-27 18:00:00"}]
        return sample_bookings
