class List:
    def remove_(self, integer_list, values_list):
        for i in values_list:
            while i in integer_list:
                integer_list.remove(i)
        return integer_list


l = List()

#https://www.codewars.com/kata/563089b9b7be03472d00002b