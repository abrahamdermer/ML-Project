from my_manager import Manager

class Meun:
    def __init__(self,adress:str,target:str|None=None):
        self.manager = Manager(adress,target)
        self._opsens = {
            '1': self.manager.get_classifi,
            '2': self.manager.get_test
        }
        self.manager.run_and_test()

    def _print_meun(self)-> None:
        print('enrer 1 to ..... \nenter 2 to ......')

    def _write_choice(self)-> str:
        _input = input()
        while _input not in self._opsens.keys():
            print('enter again')
            self._print_meun()
            _input = input()
        return _input

    def menu(self)-> None:
        self._print_meun()
        _choice =  self._write_choice()
        if _choice in self._opsens.keys():
           print(self._opsens[_choice]())

m = Meun("./newqq.csv","class")
m.menu()