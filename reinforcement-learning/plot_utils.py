import numpy as np
import matplotlib.pyplot as plt


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

def plot_values(V):
	# reshape value function
	V_sq = np.reshape(V, (4,4))

	# plot the state-value function
	fig = plt.figure(figsize=(6, 6))
	ax = fig.add_subplot(111)
	im = ax.imshow(V_sq, cmap='cool')
	for (j,i),label in np.ndenumerate(V_sq):
	    ax.text(i, j, np.round(label, 5), ha='center', va='center', fontsize=14)
	plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
	plt.title('State-Value Function')
	plt.show()