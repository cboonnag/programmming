class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list = [x for x in path.split("/") if x]
        result = list()
        for path in dir_list:
            if path =="..":
                if result:
                    result.pop()
            elif path ==".":
                pass
            else:
                result.append(path)
        return "/"+"/".join(result) 