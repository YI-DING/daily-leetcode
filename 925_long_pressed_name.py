class Solution:
    def isLongPressedName(self, name: str, typed: str):
        name_p, typed_p = 0, 0
        len_name, len_typed = len(name) - 1, len(typed) - 1
        while name_p <= len_name:
            if typed_p > len_typed:
                return False 
            if name[name_p] == typed[typed_p]:
                #move once or until not same
                if name_p < len_name and name[name_p] == name[name_p + 1]:
                    name_p += 1
                    typed_p += 1
                else:
                    while typed_p <= len_typed:
                        if typed[typed_p] == name[name_p]:
                            typed_p += 1
                        else:
                            break
                    name_p += 1
            else:
                return False
        #name ended
        if typed_p == len_typed + 1:
            return True
        for lett in typed[typed_p:]:
            if lett != name[-1]:
                return False
        return True