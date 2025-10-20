"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    cart = current_cart.copy()
    for item in items_to_add:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
    return cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable - with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for recipe_name, updated_recipe in recipe_updates:
        ideas[recipe_name] = updated_recipe
    return ideas


def sort_entries(cart):
    """Sort the items in the user cart.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    # Input validation
    if not isinstance(cart, dict):
        raise ValueError("Cart must be a dictionary.")
    if not isinstance(aisle_mapping, dict):
        raise ValueError("Aisle mapping must be a dictionary.")
    
    if not cart:
        return {}
    
    fulfillment_cart = {}
    
    # Sort items in reverse alphabetical order
    sorted_items = sorted(cart.keys(), reverse=True)
    
    for item in sorted_items:
        quantity = cart[item]
        
        # Skip invalid quantities
        if not isinstance(quantity, int) or quantity <= 0:
            continue
        
        if item in aisle_mapping:
            aisle_info = aisle_mapping[item]
            # Use the format [quantity, aisle, refrigerated] as required
            fulfillment_cart[item] = [quantity, aisle_info[0], aisle_info[1]]
        else:
            # Handle missing items - use default values
            fulfillment_cart[item] = [quantity, "Check at Counter", False]
    
    return fulfillment_cart    
def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory.
    :return: dict - store_inventory updated.
    """
    for item, order_details in fulfillment_cart.items():
        if item in store_inventory:
            ordered_quantity = order_details[0]
            current_quantity = store_inventory[item][0]
            
            if isinstance(current_quantity, int):
                new_quantity = current_quantity - ordered_quantity
                
                if new_quantity <= 0:
                    store_inventory[item][0] = 'Out of Stock'
                else:
                    store_inventory[item][0] = new_quantity
    
    return store_inventory
