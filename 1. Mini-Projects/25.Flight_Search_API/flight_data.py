class FlightData:

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        """
        FlightData 클래스의 생성자로, 특정 항공편 정보를 초기화합니다.

        Parameters:
        - price: 항공편의 가격.
        - origin_airport: 출발 공항의 IATA 코드.
        - destination_airport: 도착 공항의 IATA 코드.
        - out_date: 출발 날짜.
        - return_date: 귀국 날짜.
        - stops: 경유 횟수 (0은 직항, 1 이상은 경유 항공편).
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data):
    """
    Amadeus API에서 반환된 항공편 데이터를 분석하여 가장 저렴한 항공편을 찾는 함수.

    Args:
        data (dict): API에서 반환된 항공편 정보를 포함하는 JSON 데이터.

    Returns:
        FlightData: 가장 저렴한 항공편 정보를 담은 FlightData 객체.
        데이터가 없을 경우, 모든 필드가 'N/A'로 설정된 FlightData 객체 반환.

    이 함수는 먼저 API에서 받은 데이터가 유효한지 확인합니다. 유효한 항공편 데이터가 없으면,
    모든 필드 값이 'N/A'인 FlightData 객체를 반환합니다. 그렇지 않으면, 첫 번째 항공편을
    기준으로 가장 저렴한 항공편을 찾고, 모든 데이터를 업데이트하여 최종적으로 반환합니다.
    """

    # 데이터가 없거나 Amadeus API 요청 제한 초과 시 예외 처리
    if data is None or not data['data']:
        print("No flight data")
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
            stops="N/A"
        )

    # 첫 번째 항공편 데이터를 가져와 초기값 설정
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1  # 경유 횟수 계산
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    # 최저가 항공편 초기화
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)

    # 모든 항공편 데이터를 순회하며 최저가 항공편 찾기
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

            # 경유 횟수 업데이트 및 최저가 항공편 갱신
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight
