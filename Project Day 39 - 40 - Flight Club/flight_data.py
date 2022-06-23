
class FlightData:
    def __init__(self, price, from_city, from_airport, to_city, to_airport, from_date, return_date, stop_overs = 0, in_city = ""):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.from_date = from_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.in_city = in_city