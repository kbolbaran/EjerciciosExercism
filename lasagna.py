# Define expected bake time in minutes
EXPECTED_BAKE_TIME = 40

# Calculate remaining bake time in minutes
def bake_time_remaining(tiempo_actual):
    tiempo_total = EXPECTED_BAKE_TIME - tiempo_actual
    print(tiempo_total)

# Calculate preparation time in minutes
def preparation_time_in_minutes(number_of_layers):
    capas = number_of_layers * 2
    return capas

# Calculate total elapsed cooking time (prep + bake) in minutes
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.
    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return number_of_layers * 2 + elapsed_bake_time
