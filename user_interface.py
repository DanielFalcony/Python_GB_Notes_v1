from datetime import datetime


class Notes:
    _id = 0
    _title = ''
    _msg = ''
    _change_date = None

    def __new__(cls, *args, **kwargs):
        print('Создан новый экземпляр класса Notes')
        return super().__new__(cls)

    def __init__(self, title, msg):
        self._id += 1
        self._title = title
        self._msg = msg
        self._change_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def __str__(self):
        details = ''
        details += f'{self._id} '
        details += f'{self._title}; '
        details += f'{self._msg}; '
        details += f'{self._change_date}'
        return details

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_msg(self):
        return self._msg

    def get_change_date(self):
        return self._change_date

    def set_title(self, x):
        self._title = x

    def set_msg(self, x):
        self._msg = x

    def set_change_date(self, x):
        self._change_date = x
