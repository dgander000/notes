import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6, alpha=0.1, gamma=0.9):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.episode = 1
        self.alpha = alpha
        self.gamma = gamma

    def update_Q(self, Qsa, Qsa_next, reward, alpha, gamma):
        return Qsa + (alpha * (reward + (gamma * Qsa_next) - Qsa))
    
    def epsilon_greedy_probs(self, Q_s, i_episode, eps=None):
        epsilon = 1.0 / i_episode
        if eps is not None:
            epsilon = eps
        policy_s = np.ones(self.nA) * epsilon / self.nA
        policy_s[np.argmax(Q_s)] = 1 - epsilon + (epsilon / self.nA)
        return policy_s
        
    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        policy_s = self.epsilon_greedy_probs(self.Q[state], self.episode) 
        return np.random.choice(np.arange(self.nA), p=policy_s)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        self.Q[state][action] = self.update_Q(self.Q[state][action], np.max(self.Q[next_state]), reward, self.alpha, self.gamma)
        self.episode += 1