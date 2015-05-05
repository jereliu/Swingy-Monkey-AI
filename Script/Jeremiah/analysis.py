from ggplot import *
import pandas as pd

data_dir = "../../../Practical 4 Data/"


'''
# Analysis
'''
state_num = np.load("./data/25 x 25/e 0.01 mean 83, state 1410/state_grid_manual.npy")


'''
# 1. Generate dataset
'''

# space state travelled
state_num_np = np.array([np.array(item) for item in state_num])
state_dth_np = \
    np.concatenate(
        np.array([np.append(np.zeros(len(item)-1), 1) for item in state_num])
    ).reshape(state_num_np.shape[0], 1)

state_num_np = np.hstack([state_num_np, state_dth_np])
np.save("state_num_np.npy", state_num_np)


state_num_pd = pd.DataFrame(state_num_np,
                            columns = ["x", "p", "v", "death"])


# space state when death
state_death_np = np.array([item[-1] for item in state_num])
state_death_pd = pd.DataFrame(state_death_np,
                              columns = ["x", "p", "v"])


'''
# 1. Generate plot
'''


scatter = ggplot(state_num_pd, aes(x = "x", y = "p")) + \
          geom_point(alpha = 0.01) + \
          geom_point(state_death_pd, aes(x = "x", y = "p"),
                     colour = "red", alpha = 0.1) +\
          geom_hline(yintercept = range(-200, 201, 25),
                     colour="darkred") +\
          geom_vline(xintercept = range(-100, 351, 25),
                     colour="darkred") +\
          xlab("Horizontal Difference") + ylab("Vertical Difference")


ggsave(scatter, "./plot/s_scatter.jpg")

# velocity state travelled
vel_perc = np.percentile(state_num_pd["v"], q = range(5, 96, 10))

v_hist = ggplot(state_num_pd, aes(x = "v", fill = "death")) + \
          geom_bar() + \
          geom_vline(xintercept = vel_perc, colour="darkred")


ggsave(v_hist, "./plot/v_hist.jpg")


"describing death place/speed"

"describing common action taken (in each combination)"