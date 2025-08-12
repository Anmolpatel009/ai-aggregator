def get_fare(pickup, drop, distance_km, base_fare):
    """
    Calculate total fare for a ride.

    Args:
        pickup (str): Pickup location
        drop (str): Drop location
        distance_km (float): Distance in kilometers
        base_fare (float): Base fare in currency

    Returns:
        dict: Contains pickup, drop, and total fare
    """
    total_fare = base_fare + (distance_km * 8)  # ₹8 per km (example rate)
    return {"pickup": pickup, "drop": drop, "fare": total_fare}
