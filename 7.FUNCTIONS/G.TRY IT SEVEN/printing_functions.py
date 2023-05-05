def print_models(unprinted_designs, completed_models):
    """
     Simulate printing each design, until none are left.
     Move each design to completed_models after printing.
     """

    while unprinted_designs:
        current_models = unprinted_designs.pop()
        print(f"Printing model: {current_models}")
        completed_models.append(current_models)


def show_completed_models(completed_models):
    """ show all models that were printed """
    print("\nThe following models have been completed")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
"""
Because you moved all the design names out of unprinted_designs, the 
list is now empty, and the empty list is the only version you have; the 
original is gone. In this case, you can address this issue by passing the
function a copy of the list, not the original. Any changes the function makes 
to the list will affect only the copy, leaving the original list intact.
You can send a copy of a list to a function like this
"""

# function_name(list_name[:])

print_models(unprinted_designs[:], completed_models)
