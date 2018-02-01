def handle_keys(user_input):
    # Movement keys
    if user_input.char == 'k':
        return {'move': (0, -1)}
    elif user_input.char == 'j':
        return {'move': (0, 1)}
    elif user_input.char == 'h':
        return {'move': (-1, 0)}
    elif user_input.char == 'l':
        return {'move': (1, 0)}
    elif user_input.char == 'y':
        return {'move': (-1, -1)}
    elif user_input.char == 'u':
        return {'move': (1, -1)}
    elif user_input.char == 'b':
        return {'move': (-1, 1)}
    elif user_input.char == 'n':
        return {'move': (1, 1)}

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}