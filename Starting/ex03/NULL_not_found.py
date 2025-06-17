def NULL_not_found(object: any) -> int:
    match object:
        case object if isinstance(object, type(None)): 
            print(f"Nothing: {type(object)}")
            return 0
        case object if isinstance(object, type(float('NaN'))): 
            print(f"Cheese: {type(object)}")
            return 0
        case object if isinstance(object, type(0)): 
            print(f"Zero: {type(object)}")
            return 0
        case object if isinstance(object, type("")) and object.__len__() == 0: 
            print(f"Empty: {type(object)}")
            return 0
        case object if isinstance(object, type(False)): 
            print(f"Fake: {type(object)}")
            return 0
        
    print("type not Found")
    return 1