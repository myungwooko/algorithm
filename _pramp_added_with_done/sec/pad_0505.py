from typing import List, Text


class NoAgentFoundException(Exception):
    def error(self):
        raise Exception("not found agent")


class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load

    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


# class FinderPolicy(NoAgentFoundException):
class FinderPolicy(NoAgentFoundException):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        raise NotImplemented

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        pass


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        restrictions = ticket.restrictions
        count_pair = []

        for agent in agents:
            skills = set(agent.skills)
            count = 0
            for restriction in restrictions:
                if restriction in skills:
                    count += 1
            if count == len(restrictions):
                if not count_pair or count_pair[0][1] > agent.load:
                    count_pair = [(agent, agent.load)]

        if count_pair:
            return count_pair[0][0]
        else:
            NoAgentFoundException.error(self)


class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        restrictions = ticket.restrictions

        count_pair = []
        for agent in agents:
            skills = set(agent.skills)
            count = 0
            for restriction in restrictions:
                if restriction in skills:
                    count += 1
            if count == len(restrictions):
                if not count_pair or count_pair[0][1] > len(skills):
                    count_pair = [(agent, len(skills))]

        if count_pair:
            return count_pair[0][0]
        else:
            NoAgentFoundException.error(self)


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
agents = [agent1, agent2]



least_loaded_policy = LeastLoadedAgent()
test = least_loaded_policy.find(ticket, agents)
print(1, test)




least_flexible_policy = LeastFlexibleAgent()
test1 = least_flexible_policy.find(ticket, agents)
print(2, test1)




# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    seq = S.split(" ")
    stack = []

    for s in seq:
        print(stack)
        if s.isdigit():
            num = int(s)
            if 0 <= num <= pow(2, 20)-1:
                stack.append(int(s))
        else:
            if s == "POP":
                if stack:
                    stack.pop()
                else:
                    return -1
            elif s == "DUP":
                if stack:
                    stack.append(stack[-1])
                else:
                    return -1
            elif s == "+":
                if len(stack) > 1:
                    if stack[-2] + stack[-1] > pow(2, 20) - 1:
                        return -1
                    stack[-2] += stack[-1]
                    stack.pop()
                else:
                    return -1
            elif s == "-":
                if len(stack) > 1:
                    if stack[-1] - stack[-2] < 0:
                        return -1
                    stack[-1] -= stack[-2]
                    stack.pop(-2)
                else:
                    return -1
    return stack[-1]

S = '13 DUP 4 POP 5 DUP + DUP + -'
test = solution(S)
print(test)