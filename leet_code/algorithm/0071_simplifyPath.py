class Solution:
    def simplifyPath(self, path: str) -> str:
        ls = path.split("/")

        new_ls = ["" if x=="." else x for x in ls]
        new_path = [x for x in new_ls if (x != "")]

        n = len(new_path)
        i = 0

        while i < n:
            if (i < n-1) and (new_path[i+1] == ".."):
                new_path[i] = ""
                new_path[i+1] = ""
            if(new_path[i] == ".."):
                new_path[i] = ""
            
            i += 1
            
            if ("" in new_path):

                new_path = [value for value in new_path if value != ""]

                i = 0
                n = len(new_path)
            

        new_path = [x for x in new_path if (x != "")]    
        separater = "/"
        a = separater.join(new_path)

        return "/"+a