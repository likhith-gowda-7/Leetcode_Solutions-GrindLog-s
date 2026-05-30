class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        #we'll mark email to its index
        details=defaultdict(int)
        #this hold's index -> emails
        user_accounts=defaultdict(list)
        parent=list(range(n))
        size=[1]*n
        def find(x):
            if(parent[x]!=x):
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            x_root=find(x)
            y_root=find(y)
            if(x_root==y_root):
                return
            else:
                if(size[x_root]<size[y_root]):
                    parent[x_root]=y_root
                    size[y_root]+=size[x_root]
                else:
                    parent[y_root]=x_root
                    size[x_root]+=size[y_root]
        for idx,val in enumerate(accounts):
            user=idx
            for email in val[1:]:
                #if email is already in the details(emails), that means this email belongs to the user we have already know
                if(email in details):
                    #we'll treat index's as two separate node
                    node1=details[email]
                    node2=idx
                    #merge both user because they're same
                    union(node1,node2)
                else:
                    #else, add the information's
                    user_accounts[user].append(email)
                    details[email]=user
        for idx,node in enumerate(parent):
            root=find(idx)
            if(idx!=node):
                emails=user_accounts[idx]
                user_accounts[root].extend(emails)
                del user_accounts[idx]
        res=[]
        for node,emails in user_accounts.items():
            name=accounts[node][0]
            user=[name]
            if(emails):
                emails.sort()
                user.extend(emails)
                res.append(user)
        return res