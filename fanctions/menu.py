class Meun:
    # _opsens = {'1':print('1'),'2':print('2')}

    @staticmethod
    def _print_meun()-> None:
        print('enrer 1 to ..... \nenter 2 to ......')

    @staticmethod
    def _write_choice()-> str:
        _input = input()
        while _input not in ['1','2']:
            print('enter again')
            Meun._print_meun()
            _input = input()
        return _input

    @staticmethod
    def meun():
        Meun._print_meun()
        _choice =  Meun._write_choice()
        match _choice:
            case '1':
                print(1)
            case '2':
                print(2)

