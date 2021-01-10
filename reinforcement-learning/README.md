# Reinforcement Learning Notes

## What is reinforcement learning  
- RL is about decision making and achieving a goal
    - An agent interacts with its environment, trying to achieve some goal, and learns the best actions to take in that environment based on rewards (feedback signal) it gets from the environment   
    - An RL agent must decide what to do at each time step in its lifetime and it does this by interacting with its enviroment and learning from the feedback it gets
- Differs from other branches of machine learning
    - Supervised learning is about function approximation, mapping inputs to outputs, so you can make predictons on future inputs   
    - Unsupervised learning is about finding structure and patterns in data (groupings, clusters, etc)  
    - In RL an agent tries to maximize the reward it gets from the environment as it tries to acheive its goal
    - RL is dynamic and has a time component - if the agent is trying to solve a maze it only knows if the actions it took are correct if it actaully solves the maze

## The RL Framework
- State - Action - Reward
- State
    - Represents attributes of the environment
    - Could be location on a grid or temperature and humidity for a temperature controller
- Action
    - Agent takes an action that affects the environment
- Reward 
    - Feedback the agent gets from the environment for taking an action
- The agent is in state s and takes action a - the agent is given reward r from the environment and presented with new state s'
- This sequence repeats 
- The environement is typically the set of states the agent it trying to influence by the actions it takes
    - Modeled as a stochastic finite state machine with inputs (actions from agent) and outputs (observation and reward to agent)
    - Gridworld, Super Mario, Pong, Chess or real world
    - World in which the agent lives

## Markov Decision Processes
- The Markov Property
    - The first-order Markov assumption
    - The state of St only depends on St-1
    - The state can bet set up to encode all previous knowledge
    - For example state could be 4 consecutive screen shots
    - Observation != State
- MDP
    - discrete-time stochastic control process
    - stochastic process == random process
    - each step is discrete
    - we sample at discrete intervals so even continous processes can be considered discrete
- reward at each time step
- maximize return, G, sum of all future rewards
     - actually since future is unknown/uncertain we want to maximize the expected return
- reward is typically in the future
- RL has planning built in because agent is trying to maximize future rewards
- discount rewards further in the future (Gamma) - further in the future is harder to predict
- Value function
    - want to maximize expected (average) return - or the value function
    - value function is the expected value of the return given state s under poliicy distribution pi
    - value of a terminal state is always 0
- Recursion
    - G1 = R2 + R3 + ... + Rt
    - G2 =      R3 + ... + Rt
    - G1 = R2 + G2
    - G(t) = R(t+1) + G(t+1)
    - G(t) = R(t+1) + gamma*G(t+1)
- Bellman equation
    - State Value Function
        - V(s) = E[G(t) | St=s]
        - V(s) = E[R(t+1) + gamma*V(s') | St = s]
        - useful for evaluating a policy
    - Action Value Function
        - Q(s,a) = E[G(t) | St=s, At=a]
        - Q-table
        - useful for control - which actions to take

## Dynamic Programming


## Monte Carlo Methods


## Temporal-Difference Methods


## RL in Continuous Spaces



## Explore-Exploit Dilemma
- When comparing options or actions to take we need to collect samples and create estimates to understand which is better
- As more samples are collected the the estimates get better, the confidence interval of the estimates shrinks 
- But if we explore and up date the estimates too long we could be making sub-optimal choices longer than we need to (not exploiting what we have learned)
- Need to balance exploring and exploiting - simply choosing the highest maximum likelihood estimate (MLE) does not work
- Epsilon-Greedy
    - Greedy action - always choose the highest MLE
        - always take argmax (action with highest value)
    - Epsilon-Greedy - instead of always acting greedily there is a small probability to take some random action/choice
        - generate a random number between [0, 1]
        - if that number is less than epsilon then take a random action
        - else take argmax (action with highest value)
        - typically use a decaying epsilon since less exploration is needed over time


## Free thinking, stuff needs to be cleaned up, organized and fixed up  
RL framework  
agent interaction with environment  
agent's actions change environment   
environment is in state s, agent takes action a, the agent is presented with new state s' and reward r depending on how good/bad the action was   
sequence of s,a,r that keeps repeating   
Can be finite, or episodic, like a grid or board game  
Can be a continuous and unending   
Rewards need to be adjusted to account for this   
May want to give 0 or negative reward until goal is reached so agent gets there quickly and in the most efficient way   
Need better undersand rewards for different scenarios   
What is gamma, discount factor?  Why is it used and when?  
Modelled as an MDP   
Only previous state matters   
Need to find optimal policy   

# Terms and Lingo   
- Agent  
- State   
- Action  
- Reward
    - in gridworld could +1 for winning and -1 for losing
    - have a reward of -1 for every step so the agent tries to solve the problem quickly
- State space
    - set of all possible states
- Action space
    - set of all possible actions
- MDP - Markov Decision Process
- Episodic Tasks
    - like a gridworld
- Continuous Tasks
    - like controlling temperature of a room
- Gamma - discount factor
- Alpha - learning rate  
- Explore Exploit Dilemma
- Epsilon greedy
- Bellman Equations 
- Dynamic Programming   
- Policy
    - maps states to actions
    - can be a computer program, equation, neural network
    - can be probabilistic or deterministic
- Optimal Policy
- Convergence
- Model based
- Model free
- State value function
- Action value function
- Value iteration
- Policy iteration
- Policy evaluation
- Monte Carlo methods
- Temporal Difference Learning
- SARSA
- SARSA Max - Q learning
- Q-table
- Function approximation
- Tile coding



