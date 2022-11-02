import pyautogui
import keyboard


class PianoTiles:
    def __init__(self):
        print('Apasa TASTA ESC pentru a inchide programul')
        x1 = self._mouse_pos('STANGA')[0]

        while keyboard.is_pressed('enter'):
            pass

        x2 = self._mouse_pos('DREAPTA')[0]
        self.left_x, self.right_x = min(x1, x2), max(x1, x2)
        self.center_y = pyautogui.size()[1] // 2
        self.tiles = self._tiles_pos()
        print(f'Coordonatele jocului sunt {self.left_x}, {self.right_x}, {self.center_y}')

    def _mouse_pos(self, border):
        print(f'Pune cursorul in {border} marginii ferestrei jocului si apasa ENTER')

        while not (keyboard.is_pressed('enter') or keyboard.is_pressed('esc')):
            x, y = pyautogui.position()
            print(f'X: {str(x).rjust(4)}\tY: {str(y).rjust(4)}', end='\r')

        print(f'{border} border: {x}, {y}')
        return x, y

    def _tiles_pos(self):
        lenght = self.right_x - self.left_x
        step = lenght // 4
        return [
            (self.left_x + i, self.center_y) for i in range(step // 2, lenght, step)
        ]

    def _is_tile(self, pixel, threshold):
        return pyautogui.pixel(*pixel)[0] <= threshold

    def run(self, *, tile_rgb=10):
        while not keyboard.is_pressed('esc'):
            for pos in self.tiles:
                if self._is_tile(pos, tile_rgb):
                    pyautogui.click(*pos)
                    break


if __name__ == '__main__':
    PianoTiles().run()
