import pygame

class Input:
    _keys_down = set()
    _keys_held = set()
    _mouse_buttons_down = set()
    _mouse_buttons_held = set()
    _mouse_pos = (0, 0)

    @staticmethod
    def update(events):
        Input._keys_down.clear()
        Input._mouse_buttons_down.clear()

        for event in events:
            if event.type == pygame.KEYDOWN:
                Input._keys_down.add(event.key)
                Input._keys_held.add(event.key)

            elif event.type == pygame.KEYUP:
                if event.key in Input._keys_held:
                    Input._keys_held.remove(event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                Input._mouse_buttons_down.add(event.button)
                Input._mouse_buttons_held.add(event.button)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in Input._mouse_buttons_held:
                    Input._mouse_buttons_held.remove(event.button)

        Input._mouse_pos = pygame.mouse.get_pos()

    @staticmethod
    def get_key_down(key):
        return key in Input._keys_down

    @staticmethod
    def get_key_held(key):
        return key in Input._keys_held

    @staticmethod
    def get_mouse_button_down(button):
        return button in Input._mouse_buttons_down

    @staticmethod
    def get_mouse_button_held(button):
        return button in Input._mouse_buttons_held

    @staticmethod
    def get_mouse_position():
        return Input._mouse_pos
