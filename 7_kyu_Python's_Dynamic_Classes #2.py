class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        assert new_name[0].isupper() and new_name.isalnum()
        cls.__name__ = new_name

    @classmethod
    def __str__(cls):
        return "Class name is: {}".format(cls.__name__)

#https://www.codewars.com/kata/55ddcef532f8678af1000006