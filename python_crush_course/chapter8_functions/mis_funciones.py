# Function to simulate printing 3D models

def print_models(unprinted_models, completed_models):
    """
    Simulate 3D printing of each model until none are left
    Move each design to completed_models after printing
    :param unprinted_models: Models that need to be 3D printed
    :param completed_models: Models that have been 3D printed
    :return: nothing
    """
    while unprinted_models:
        current_model = unprinted_models.pop()
        print("3D Printing: {}".format(current_model))
        completed_models.append(current_model)


def show_completed_models(completed_models):
    """
    Show all completed models
    :param completed_models: Models that have been 3D printed
    :return: nothing
    """
    for model in completed_models:
        print("Model printed: {}".format(model))
