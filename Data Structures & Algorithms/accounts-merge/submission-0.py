from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)

        rank = [1] * n
        parent = [i for i in range(n)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return

            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            elif rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            else:
                parent[rootA] = rootB
                rank[rootB] += 1

        # email -> first account index containing that email
        merge = {}

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]

                if email not in merge:
                    merge[email] = i
                else:
                    # The same email appeared in another account
                    union(i, merge[email])

        # root account index -> all emails belonging to it
        emails = defaultdict(list)

        for email, accountIndex in merge.items():
            user_id = find(accountIndex)
            emails[user_id].append(email)

        result = []

        for user_id, user_emails in emails.items():
            name = accounts[user_id][0]
            result.append([name] + sorted(user_emails))

        return result