def simplifyPath(self, path):
    if not path or path == '/../':
        return '/'
    #if path[0] is not '/':
    #    return None
    new=path.split("/")
    result=[]
    for unit in new:
        if not unit or unit == '.':
            continue 
        if unit == '..':
            if not result:
                continue 
            else:
                result.pop()
        else:
            result.append(unit)
    return '/'+'/'.join(result)