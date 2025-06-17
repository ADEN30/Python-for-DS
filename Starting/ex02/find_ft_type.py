def all_thing_is_obj(object: any) -> int:
    match object:
        case object if isinstance(object, list): print(f"List: {type(object)}")
        case object if isinstance(object, tuple): print(f"Tuple: {type(object)}")
        case object if isinstance(object, set): print(f"Set: {type(object)}")
        case object if isinstance(object, dict): print(f"Dict: {type(object)}")
        case object if isinstance(object, str): print(f'{object} is in the kitchen : {type(object)}')
        case object if isinstance(object, int): print("Type not find")
    return 42