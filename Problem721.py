# https://leetcode.com/problems/accounts-merge/
# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0]
# is a name, and the rest of the elements are emails representing emails of the account.
#
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common
# email to both accounts. Note that even if two accounts have the same name, they may belong to different people as
# people could have the same name. A person can have any number of accounts initially, but all of their accounts
# definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the first element of each account is the
# name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
import collections
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email_to_names = dict()
        graph = collections.defaultdict(set)

        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            first_email = acc[1]
            for email in emails:
                email_to_names[email] = name
                # build graph where 1st email is linked to all others emails from this account
                graph[email].add(first_email)
                # and vice versa
                graph[first_email].add(email)

        visited = set()
        answer = []
        for email in graph.keys():
            if email in visited:
                continue
            visited.add(email)

            # look for linked components in graph containing given email
            linked_graph_component = set()
            linked_graph_component.add(email)

            stack = [email]

            while len(stack) > 0:
                current = stack.pop()
                for neighbour in graph[current]:
                    if neighbour not in visited:
                        stack.append(neighbour)
                        linked_graph_component.add(neighbour)
                        visited.add(neighbour)

            name = email_to_names[email]
            answer.append([name] + sorted(linked_graph_component))

        return answer
