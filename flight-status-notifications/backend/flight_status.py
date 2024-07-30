def get_flight_status(flight_id):
    # Mock data for demonstration
    flights = {
        "AB123": {"status": "On Time", "gate": "A1"},
        "CD456": {"status": "Delayed", "gate": "B2"},
    }
    return flights.get(flight_id, None)
