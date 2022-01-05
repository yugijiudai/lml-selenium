class SeleniumDto:
    __slots__ = ('__id', '__description', '__model', '__element_action', '__element', '__find_type',
                 '__wait', '__retry', '__click_action', '__valid', '__ext', '__call_back')

    def __init__(self):
        self.__id = None
        self.__description = None
        self.__model = None
        self.__element_action = None
        self.__element = None
        self.__find_type = None
        self.__wait = None
        self.__retry = None
        self.__click_action = None
        self.__valid = None
        self.__ext = None
        self.__call_back = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def element_action(self):
        return self.__element_action

    @element_action.setter
    def element_action(self, value):
        self.__element_action = value

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, value):
        self.__element = value

    @property
    def find_type(self):
        return self.__find_type

    @find_type.setter
    def find_type(self, value):
        self.__find_type = value


    @property
    def wait(self):
        return self.__wait

    @wait.setter
    def wait(self, value):
        self.__wait = value

    @property
    def retry(self):
        return self.__retry

    @retry.setter
    def retry(self, value):
        self.__retry = value

    @property
    def click_action(self):
        return self.__click_action

    @click_action.setter
    def click_action(self, value):
        self.__click_action = value

    @property
    def valid(self):
        return self.__valid

    @valid.setter
    def valid(self, value):
        self.__valid = value

    @property
    def ext(self):
        return self.__ext

    @ext.setter
    def ext(self, value):
        self.__ext = value

    @property
    def call_back(self):
        return self.__call_back

    @call_back.setter
    def call_back(self, value):
        self.__call_back = value

    def to_dict(self):
        return {
            "id": self.__id,
            "description": self.__description,
            "model": self.__model,
            "element_action": self.__element_action,
            "element": self.__element,
            "find_type": self.__find_type,
            "wait": self.__wait,
            "retry": self.__retry,
            "click_action": self.__click_action,
            "valid": self.__valid,
            "ext": self.__ext,
            "call_back": self.__call_back,
        }
