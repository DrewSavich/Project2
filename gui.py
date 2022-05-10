from tkinter import *
from weather_class import *

class GUI:
    def __init__(self, window) -> None:
        """
        Initializes the display for the report
        :param window: the essential frame for creating the display
        """
        self.window = window
        choices = ["Temperature", "Wind Speeds", "Humidity", "Sunrise/Sunset"]

        self.frame_display = Frame(self.window)
        self.label_display = Label(self.frame_display, text='Welcome to Weather Report')
        self.label_request = Label(self.frame_display, text='Please Enter a City')
        self.entry_request = Entry(self.frame_display)
        self.button_entry = Button(self.frame_display, text='SUBMIT', command=self.clicked)
        self.label_check = Label(self.frame_display, text='')
        self.window.resizable(False, False)

        self.frame_display.pack(anchor='n')
        self.label_display.pack(side='top')
        self.label_request.pack(side='top')
        self.entry_request.pack(side='top')
        self.button_entry.pack(side='top', pady=5)
        self.label_check.pack(side='top')

        self.frame_list = Frame(self.window)
        self.label_list = Label(self.frame_list, text='Please choose an option')
        self.click = StringVar()
        self.click.set('Temperature')
        self.drop_list = OptionMenu(self.frame_list, self.click, *choices)

        self.frame_list.pack(anchor='w', pady=5)
        self.label_list.pack(side='left')
        self.drop_list.pack(side='left')

        self.frame_result = Frame(self.window)
        self.button_result = Button(self.frame_result, text='SUBMIT', command=self.list_result, state=DISABLED)
        self.label_result = Label(self.frame_result, text='\n\n\n')

        self.frame_result.pack(anchor='n')
        self.button_result.pack(side='top')
        self.label_result.pack(side='top')

        self.frame_reset = Frame(self.window)
        self.label_reset = Label(self.frame_reset, text='Click NEW to re-enter a city')
        self.button_reset = Button(self.frame_reset, text='NEW', state=DISABLED, command=self.reset)

        self.frame_reset.pack(anchor='s')
        self.button_reset.pack(side='bottom')
        self.label_reset.pack(side='bottom')


    def clicked(self):
        city = self.entry_request.get()
        report = Weather(city)
        if report.result_check() == 'Invalid':
            self.label_check['text'] = "Invalid Entry - Please enter a valid city"
            self.entry_request.delete(0, END)
        elif report.result_check() == 'Valid':
            self.entry_request['state'] = DISABLED
            self.button_entry['state'] = DISABLED
            self.button_result['state'] = ACTIVE
            self.button_reset['state'] = ACTIVE
            self.label_check['text'] = ''

    def list_result(self):
        city = self.entry_request.get()
        new_report = Weather(city)
        if self.click.get() == 'Temperature':
            self.label_result['text'] = new_report.temp() + '\n'
        elif self.click.get() == 'Wind Speeds':
            self.label_result['text'] = new_report.wind() + '\n\n'
        elif self.click.get() == 'Humidity':
            self.label_result['text'] = new_report.humid() + '\n\n'
        elif self.click.get() == 'Sunrise/Sunset':
            self.label_result['text'] = new_report.suntime() + '\n\n'

    def reset(self):
        self.entry_request['state'] = NORMAL
        self.entry_request.delete(0, END)
        self.label_result['text'] = '\n\n\n'
        self.button_entry['state'] = ACTIVE
        self.button_result['state'] = DISABLED

