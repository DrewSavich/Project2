# Original code: https://www.youtube.com/watch?v=9P5MY_2i7K8
# Features include: Options for displaying main results, relocation button choice
from gui import *


def main() -> None:
    """
    Established the display from GUI
    """
    window = Tk()
    window.title('Weather Report')
    window.geometry('300x340')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
