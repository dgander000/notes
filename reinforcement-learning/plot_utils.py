import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns
sns.set_style("white")

def plot_blackjack_values(V):

    def get_Z(x, y, usable_ace):
        if (x,y,usable_ace) in V:
            return V[x,y,usable_ace]
        else:
            return 0

    def get_figure(usable_ace, ax):
        x_range = np.arange(11, 22)
        y_range = np.arange(1, 11)
        X, Y = np.meshgrid(x_range, y_range)
        
        Z = np.array([get_Z(x,y,usable_ace) for x,y in zip(np.ravel(X), np.ravel(Y))]).reshape(X.shape)

        surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, vmin=-1.0, vmax=1.0)
        ax.set_xlabel('Player\'s Current Sum')
        ax.set_ylabel('Dealer\'s Showing Card')
        ax.set_zlabel('State Value')
        ax.view_init(ax.elev, -120)

    fig = plt.figure(figsize=(20, 20))
    ax = fig.add_subplot(211, projection='3d')
    ax.set_title('Usable Ace')
    get_figure(True, ax)
    ax = fig.add_subplot(212, projection='3d')
    ax.set_title('No Usable Ace')
    get_figure(False, ax)
    plt.show()

def plot_policy(policy):

    def get_Z(x, y, usable_ace):
        if (x,y,usable_ace) in policy:
            return policy[x,y,usable_ace]
        else:
            return 1

    def get_figure(usable_ace, ax):
        x_range = np.arange(11, 22)
        y_range = np.arange(10, 0, -1)
        X, Y = np.meshgrid(x_range, y_range)
        Z = np.array([[get_Z(x,y,usable_ace) for x in x_range] for y in y_range])
        surf = ax.imshow(Z, cmap=plt.get_cmap('Pastel2', 2), vmin=0, vmax=1, extent=[10.5, 21.5, 0.5, 10.5])
        plt.xticks(x_range)
        plt.yticks(y_range)
        plt.gca().invert_yaxis()
        ax.set_xlabel('Player\'s Current Sum')
        ax.set_ylabel('Dealer\'s Showing Card')
        ax.grid(color='w', linestyle='-', linewidth=1)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.1)
        cbar = plt.colorbar(surf, ticks=[0,1], cax=cax)
        cbar.ax.set_yticklabels(['0 (STICK)','1 (HIT)'])
            
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(121)
    ax.set_title('Usable Ace')
    get_figure(True, ax)
    ax = fig.add_subplot(122)
    ax.set_title('No Usable Ace')
    get_figure(False, ax)
    plt.show()

def plot_values(V):
	# reshape the state-value function
	V = np.reshape(V, (4,12))
	# plot the state-value function
	fig = plt.figure(figsize=(15,5))
	ax = fig.add_subplot(111)
	im = ax.imshow(V, cmap='cool')
	for (j,i),label in np.ndenumerate(V):
	    ax.text(i, j, np.round(label,3), ha='center', va='center', fontsize=14)
	plt.tick_params(bottom='off', left='off', labelbottom='off', labelleft='off')
	plt.title('State-Value Function')
	plt.show()

# def plot_values(V):
# 	# reshape value function
# 	V_sq = np.reshape(V, (4,4))

# 	# plot the state-value function
# 	fig = plt.figure(figsize=(6, 6))
# 	ax = fig.add_subplot(111)
# 	im = ax.imshow(V_sq, cmap='cool')
# 	for (j,i),label in np.ndenumerate(V_sq):
# 	    ax.text(i, j, np.round(label, 5), ha='center', va='center', fontsize=14)
# 	plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
# 	plt.title('State-Value Function')
# 	plt.show()

def map_env(env, title=None):
	shape = env.desc.shape
	nRows = shape[0] # rows
	nCols = shape[1] # columns

	# create the heatmap
	heat_map = np.zeros(shape)
	for i in range(nRows):
		for j in range(nCols):
			if env.desc[i, j] == b'H':
				heat_map[i, j] = 0.25  # make holes colder
			elif env.desc[i, j] == b'G':
				heat_map[i, j] = 1.    # make goal hotter

	fig, ax = plt.subplots(figsize=(6,6))
	im = ax.imshow(heat_map, cmap='cool')

	# create the grid lines
	ax.set_xticks(np.arange(nCols))
	ax.set_yticks(np.arange(nRows))
	ax.set_xticklabels(np.arange(nCols))
	ax.set_yticklabels(np.arange(nRows))
	ax.set_xticks(np.arange(-0.5, nCols, 1), minor=True)
	ax.set_yticks(np.arange(-0.5, nRows, 1), minor=True)
	ax.grid(False)
	ax.grid(which='minor', color='w', linewidth=2)

	# add state description and number
	offset = 0.35
	for i in range(env.nS):
		y = i//nRows # row
		x = i%nCols  # column

		if (x, y) == (0, 0):
			ax.text(x, y, 'S ', ha='center', va='center', color='k', size=18)
		elif env.desc[y, x] == b'H':
			ax.text(x, y, 'x', ha='center', va='center', color='k', size=18)
		elif env.desc[y, x] == b'G':
			ax.text(x, y, 'G', ha='center', va='center', color='k', size=18)
		else:
			pass
		ax.text(x, y+offset, str(i), ha='center', va='center', color='k', size=10)

	fig.tight_layout()
	if title:
		ax.set_title(title)
	plt.show()

def plot_V(env, V, title=None):
	shape = env.desc.shape
	nRows = shape[0] # rows
	nCols = shape[1] # columns

	# create the heatmap
	heat_map = np.zeros(shape)
	for i in range(nRows):
		for j in range(nCols):
			if env.desc[i, j] == b'H':
				heat_map[i, j] = 0.25  # make holes colder
			elif env.desc[i, j] == b'G':
				heat_map[i, j] = 1.    # make goal hotter

	fig, ax = plt.subplots(figsize=(6,6))
	im = ax.imshow(heat_map, cmap='cool')

	# create the grid lines
	ax.set_xticks(np.arange(nCols))
	ax.set_yticks(np.arange(nRows))
	ax.set_xticklabels(np.arange(nCols))
	ax.set_yticklabels(np.arange(nRows))
	ax.set_xticks(np.arange(-0.5, nCols, 1), minor=True)
	ax.set_yticks(np.arange(-0.5, nRows, 1), minor=True)
	ax.grid(False)
	ax.grid(which='minor', color='w', linewidth=2)

	# add state description, number and value
	offset = 0.35
	for i in range(env.nS):
		y = i // nRows # row
		x = i % nCols  # column

		if (x, y) == (0, 0):
			ax.text(x, y-offset, 'S ', ha='center', va='center', color='k', size=14)
		elif env.desc[y, x] == b'H':
			ax.text(x, y-offset, 'x', ha='center', va='center', color='k', size=14)
		elif env.desc[y, x] == b'G':
			ax.text(x, y-offset, 'G', ha='center', va='center', color='k', size=14)
		else:
			pass
		ax.text(x, y+offset, str(i), ha='center', va='center', color='k', size=10)
		ax.text(x, y, np.round(V[i], 4), ha='center', va='center', color='k', size=14)

	fig.tight_layout()
	if title:
		ax.set_title(title)
	plt.show()

def map_actions(env, states, actions, title=None):
	mapping = {
		0: '<',
		1: 'v',
		2: '>',
		3: '^'
	}

	shape = env.desc.shape
	nRows = shape[0] # rows
	nCols = shape[1] # columns

	# create the heatmap
	heat_map = np.zeros(shape)
	for i in range(nRows):
		for j in range(nCols):
			if env.desc[i, j] == b'H':
				heat_map[i, j] = 0.25  # make holes colder
			elif env.desc[i, j] == b'G':
				heat_map[i, j] = 1.    # make goal hotter

	fig, ax = plt.subplots(figsize=(6,6))
	im = ax.imshow(heat_map, cmap='cool')

	# create the grid lines
	ax.set_xticks(np.arange(nCols))
	ax.set_yticks(np.arange(nRows))
	ax.set_xticklabels(np.arange(nCols))
	ax.set_yticklabels(np.arange(nRows))
	ax.set_xticks(np.arange(-0.5, nCols, 1), minor=True)
	ax.set_yticks(np.arange(-0.5, nRows, 1), minor=True)
	ax.grid(False)
	ax.grid(which='minor', color='w', linewidth=2)

	# add state description and number
	offset = 0.35
	for i in range(env.nS):
		y = i // nRows # row
		x = i % nCols  # column

		if (x, y) == (0, 0):
			ax.text(x, y-offset, 'S ', ha='center', va='center', color='k', size=16)
		elif env.desc[y, x] == b'H':
			ax.text(x, y-offset, 'x', ha='center', va='center', color='k', size=16)
		elif env.desc[y, x] == b'G':
			ax.text(x, y-offset, 'G', ha='center', va='center', color='k', size=16)
		else:
			pass
		ax.text(x, y+offset, str(i), ha='center', va='center', color='k', size=10)

	# add action
	for i, action in enumerate(actions):
		y = states[i] // nRows # row
		x = states[i] % nCols  # column
		ax.text(x, y, mapping[action], ha='center', va='center', color='k', size=18)

	fig.tight_layout()
	if title:
		ax.set_title(title)
	plt.show()

