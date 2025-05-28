def strict(func):
    def wrapper(*args, **kwargs):
        func_annotations = func.__annotations__
        if len(args) != len(func_annotations) - 1:
            raise TypeError(f"В функцию переданы не все аргументы")
        for arg_name, arg_value in zip(func_annotations.keys(), args):
            expected_type = func_annotations[arg_name]
            if not isinstance(arg_value, expected_type):
                raise TypeError(f"Аргумент '{arg_name}' должен быть типом {expected_type.__name__}, а является {type(arg_value).__name__}")
        return func(*args, **kwargs)
    
    return wrapper
