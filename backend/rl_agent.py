import random

actions = ["deploy", "retry", "stop"]

# Q-table (simple dictionary)
Q = {}

def get_state(risk):
    if risk < 0.3:
        return "low"
    elif risk < 0.7:
        return "medium"
    else:
        return "high"

def choose_action(state):
    if state == "low":
        return "deploy"
    elif state == "medium":
        return "retry"
    else:
        return "stop"

    # ε-greedy strategy
    if random.random() < 0.2:
        return random.choice(actions)

    return actions[Q[state].index(max(Q[state]))]