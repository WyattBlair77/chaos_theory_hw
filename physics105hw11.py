import matplotlib.pyplot as plt
import numpy as np


# Define logistic map function
def f(x, r):
    return r*x*(1-x)


# Use recursion to generate the set of x's
def iter_f(r, current_list, interval, step=1):
    if interval == step:
        new_list = current_list
        return new_list
    elif step < interval:
        new_val = f(current_list[-1], r)
        current_list.append(new_val)
        return iter_f(r, current_list, interval, step+1)


# plot the function f with a given value of r for the interval
def plot_f(r, interval=30):
    time = np.arange(0, interval)
    f_data = iter_f(r, [0.1], interval)

    fig, ax = plt.subplots()
    ax.plot(time, f_data)
    plt.show()


# Plot the theoretical bifurcation diagram
def plot_bifurcation_theoretical(ax):
    r_range = np.arange(0, 4, 0.1)

    x1 = np.zeros(40)
    x1_stable = x1[0:10]
    x1_unstable = x1[10:]

    x2 = [(r-1)/r for r in r_range]
    x2_stable = x2[10:30]
    x2_unstable = x2[30:]

    ax.plot(r_range[0:10], x1_stable, color='pink')
    ax.plot(r_range[10:], x1_unstable, linestyle='--', color='pink')
    ax.plot(r_range[10:30],  x2_stable, color='blue')
    ax.plot(r_range[30:], x2_unstable, linestyle='--', color='blue')


# Plot the experimental bifurcation diagram
# Arrived at value for t_max because the recursive depth limit was 994
def plot_bifurcation_experimental(ax, r_min=0.0, r_max=4.0, step=0.1, x0=0.1):
    r_range = np.arange(r_min, r_max, step)
    t_max = 994
    t_min = 900

    for r in r_range:
        f_data = iter_f(r, [x0], t_max)[t_min:]
        r_vals = np.array([r for i in range(len(f_data))])
        ax.scatter(r_vals, f_data, s=1, marker='.', color='black')


# Question 1)
# I used recursion to generate all the different steps of the logistics map. I believe this sped up my program and
# allows it to be scalable as we move further throughout the problem set. However, this does limit the M (or t_max)
# value allowable by my computer to 994 before the stack overflows. This means for every r value, t_max - t_min = 94
# x values are plotted.
fig1, ax = plt.subplots()
ax.set_xlabel('r')
ax.set_ylabel('x')
ax.set_title('Physics 105 Homework 11 Question 1')
plot_bifurcation_theoretical(ax)
plot_bifurcation_experimental(ax)
plt.savefig('question1.png')
plt.show()


# Question 2)
# Just needed to adjust my r_min and r_max, which define my r_range variable in the plot_bifurcation_experimental()
# function. Also, to get a crisper picture I adjusted the step between the r values.
fig2, ax = plt.subplots()
ax.set_xlabel('r')
ax.set_ylabel('x')
ax.set_title('Physics 105 Homework 11 Question 2')
plot_bifurcation_experimental(ax, r_min=2.8, r_max=4.0, step=0.01)
plt.savefig('question2.png')
plt.show()


# Question 3)
# Did not encounter any new challenges. I just started my recursive function with a different seed and
# generated all the fixed points around there. Then I clipped the y-axis to only show one branch
fig3, ax = plt.subplots()
ax.set_xlabel('r')
ax.set_ylabel('x')
ax.set_title('Physics 105 Homework 11 Question 3')
plot_bifurcation_experimental(ax, r_min=3.84, r_max=3.86, step=0.0001, x0=0.4578)
ax.set_ylim(0.44, 0.56)
plt.savefig('question3')
plt.show()


# Question 4)
# There is a new flipping over here. It seems there are some noisy x's around the edges
# are those the numerical issue the question references? I would say those are just pieces
# of another branch intersecting with this one.
fig4, ax = plt.subplots()
ax.set_xlabel('r')
ax.set_ylabel('x')
ax.set_title('Physics 105 Homework 11 Question 4')
plot_bifurcation_experimental(ax, r_min=3.8537, r_max=3.8542, step=0.000001, x0=0.489)
ax.set_ylim(0.4895, 0.5085)
plt.savefig('question4.png')
plt.show()
