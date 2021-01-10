# Learning Machine Learning   
Repo for my adventures in learning machine learning.    

### What is machine learning?   
- Ability for a computer program to  learn a task without being explicitly programmed to do so by getting better through experience.  
- Formal definition by [Tom Mitchell](http://www.cs.cmu.edu/afs/cs.cmu.edu/user/mitchell/ftp/mlbook.html):   
	A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E.    
- A technique for performing inductive bias (observing specific instances and forming a general rule from them).  As opposed to deductive reasoning which proposes general hypotheses and then observes specific instances that either support or reject it.

### Main categories of machine learning   
- supervised learning     
	- function approximation (generalize)  
	given inputs and corresponding output -> generalize (build model) -> then given new inputs predict their output   
	[X, y] ---generalize---> f(X) ---predict---> f(X') -> y'   
	- fundamental problem is generalization and finding a function that labels the data well   
	- assumptions
		- the function is well behaved, consistent with the data and able to generalize
		- the data you have accurately represents the problem space     
- unsupervised learning    
	- just have inputs and need to derive some structure   
	- about creating descriptions, summaries, clusters (should cluster data well)    
	- X -> cluster -> [y1, y2, ... yn]      
	- can be used with supervised learning   
	inputs -> descriptions (u.l.) -> summaries -> function approximation (s.l.) -> labels
- reinforcement learning     
	-  learning a behavior, from delayed reward, that performs well    
	-  like playing a game without the knowing rules/how to win and occasionally being told how you're doing   

### Machine Learning Terminology  
- Instances (set of inputs)   
Vectors of attributes (features) that define the input space (e.g. pixel values of a picture, credit score examples containing income, debt, etc)
- Concept  
	- A function that maps inputs to outputs
	- Can have multiple concepts        
	- A mapping between objects in the world and membership in a set (e.g. if you have concept of a car, if given something you know if it's a car or not).    
- Target Concept  
The actual answer we are searching for in the space of multiple concepts (hypothesis class).  (e.g. the function that determines if something is a car or not)  
- Hypothesis class  
The set of all concepts you're trying to entertain. Could be all possible functions (however, given finite data, an infinite space to search).   
- Training set (samples)
	- Examples of input output pairs (e.g., person info (income, debt) and credit worthiness)    
	- Basis for determining best concept/function (used to learn best concept/function)      
- Candidate    
A concept that is believed to be the target concept (e.g., a specific decision tree)       
- Testing Set
	- Structure just like training set  
	- Take candidate and determine if it does a good job by looking at error when testing set is applied to the candidate  
	- Testing and Training set never overlap.  Never train from testing set!     
	- Should contain lots of examples not seen in the training set   

### Bias  
Biases when thinking about algorithms searching through space:   
*Restriction bias*   
- Hypothesis set you care about (e.g., all possible decision trees)   
- Describes the hypothesis set space $H$ that is considered for the learning effort (e.g., decision trees and not quadratic equations).   

*Preference bias*  
- What sort of hypothesis from the hypothesis set are preferred   
- Describes the subset of hypotheses, $n$, from the hypothesis set space that we *prefer* ($n \in H$), which is really at the heart of inductive bias.    
