class Phone:
    numberstart: int = 000
    _calling: int = 0

    def setnumber(self, number: int):
        self.number = self.numberstart
        return f' {number}'

    def how_match_income_calling(self):
        return self._calling
    print(f'{_calling}')

    def incoming_call(self):
        self._calling += 1
        return self._calling


telephone_1 = Phone()
telephone_2 = Phone()
telephone_3 = Phone()
number1 = telephone_1.setnumber(111)
number2 = telephone_2.setnumber(222)
number3 = telephone_3.setnumber(333)
print(f'Для телефона установлен номер {number1}')
telephone_1.incoming_call()
telephone_1.incoming_call()
telephone_2.incoming_call()
telephone_2.incoming_call()
telephone_2.incoming_call()
telephone_3.incoming_call()
telephone_3.incoming_call()
telephone_3.incoming_call()
telephone_3.incoming_call()

print(f'на телефон 1 позвонили {telephone_1.how_match_income_calling()} раза')
print(f'на телефон 2 позвонили {telephone_2.how_match_income_calling()} раза')
print(f'на телефон 3 позвонили {telephone_3.how_match_income_calling()} раза ')

'''Напишите функцию, которая принимает список из объектов телефонов, а возвращает общее кол-во принятых
звонков со всех телефонов.'''


class AllColl(Phone):
    all_phone = (telephone_1, telephone_2, telephone_3)

    def list_calls_in_telephone(self):
        list_call = [telephone_1.how_match_income_calling(), telephone_2.how_match_income_calling(),
            telephone_3.how_match_income_calling()]
        return print(sum(list_call))


k = AllColl()
k.list_calls_in_telephone()
