class Solution:
    def decodeString(self, s: str) -> str:
        res=""
        st=[]
        for i in s:
            if(i=="]"):
                en=""
                c=""
                while st and st[-1]!="[":
                    en=st.pop()+en
                st.pop()
                while st and st[-1].isdigit():
                    c=st.pop()+c
                res=int(c)*en
                st.append(res)
            else:
                st.append(i)
        return "".join(st)