class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        fields={"electronics":[],"grocery":[],"pharmacy":[],"restaurant":[]}
        def check(s):
            for ch in s:
                if(ch!="_" and not ch.isalnum()):
                    return  False
            return True
        for idx in range(len(code)):
            coupon=code[idx]
            business=businessLine[idx]
            state=isActive[idx]
            if(not coupon or (business not in fields) or not state):
                continue
            elif(check(coupon)):
                fields[business].append(coupon)
        valids=[]
        for key,val in fields.items():
            if(val):
                valids.extend(sorted(val))
        return valids


