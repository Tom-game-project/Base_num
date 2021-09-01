

class IndexStringLengthError(BaseException):
    """
    lengthError
    index string must be length 1
    """
    pass


class ListLengthError(BaseException):
    """
    """
    pass


class Base_num:
    """
    Base Number module
    ===
    """
    numbers: list[str] = [str(i) for i in range(10)]+[chr(i)
                                                      for i in range(ord("a"), ord("z")+1)]
    BIN: int = 2
    OCT: int = 8
    HEX: int = 16

    def __init__(self, base_number: str, base: int = 10) -> None:
        self.base_number: str = str(base_number)
        self.base: int = base
        self.decimal: int = self.__b_t_d(self.base_number, self.base)

    def __b_t_d(self, num: str, base: int) -> int:
        rint = 0
        for i, j in enumerate(str(num)):
            rint += (base**i)*self.numbers.index(j)
        return rint

    def __d_t_b(self, num: str, base: int) -> "Base_num":
        if len(self.numbers) < base:
            raise ListLengthError(
                f"Conversion list must be longer than {base}")
        divide = num
        rlist = []
        while int(divide):
            rlist.append(divide % base)
            divide /= base
            divide = int(divide)
        return Base_num("".join([self.numbers[i] for i in rlist[::-1]]), base=base)

    @classmethod
    def decimal_to_basenum(cls, num: int, base: int) -> "Base_num":
        """
        10進数からn進数に変換
        """
        if len(cls.numbers) < base:
            raise ListLengthError(
                f"Conversion list must be longer than {base}")
        divide = num
        rlist = []
        while int(divide):
            rlist.append(divide % base)
            divide //= base
        return Base_num("".join([cls.numbers[i] for i in rlist[::-1]]), base=base)

    @staticmethod
    def set_numbers_list(new_list: list[str]) -> None:
        """
        change default Conversion list
        ---
        argument must be list 
        index string of length 1\n
        
        ===example===
        ```python
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ```
        ============
        """
        for i in new_list:
            type_ = type(i)
            if type_ is str:
                pass
            else:
                raise TypeError(
                    f"init_numbers_list() expected string of length 1, but {type_} found")
        for i in new_list:
            len_ = len(i)
            if len_ == 1:
                pass
            else:
                raise IndexStringLengthError(
                    f"init_numbers_list() expected string of length 1, but length {len_}")
        Base_num.numbers: list[str] = new_list

    @staticmethod
    def set_numbers_list_default() -> None:
        numbers: list[str] = [str(i) for i in range(10)]+[chr(i)
                                                          for i in range(ord("a"), ord("z")+1)]

    def __add__(self, other):
        d = self.decimal+other.decimal
        return self.__d_t_b(d, self.base)

    def __sub__(self, other):
        d = self.decimal+other.decimal
        return self.__d_t_b(d, self.base)

    def __mul__(self, other):
        d = self.decimal+other.decimal
        return self.__d_t_b(d, self.base)

    def __floordiv__(self, other):
        d = self.decimal // other.decimal
        return self.__d_t_b(d, self.base)
