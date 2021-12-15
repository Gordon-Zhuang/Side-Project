#-o---T
# T 為終點, o 是探索者的位置

import numpy as np
import pandas as pd
import time
import random

N_STATES = 5                                # 每個维度的長度
ACTIONS = ['left', 'right', 'up', 'down']     # 探索者可以使用的動作
EPSILON = 0.9                                 # 貪婪度 greedy
ALPHA = 0.9                                   # 學習率
GAMMA = 0.3                                   # 獎勵遞減律
MAX_EPISODES = 1000                            # 迭代次數
FRESH_TIME = 0.4                          # 每一步移動間格時間

STEP_ARRAY = []

def build_q_table(n_states, actions):
    step = [str(i)+str(j) for i in range(N_STATES) for j in range(N_STATES)]
    n_states = n_states*n_states
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),
        index=step,
        columns=actions,                      # columns 對應行為名稱
    )
    table += 0.5                              # 將q_table 初始為0.5(將加權機率賦予初值)
    return table

# q_table:
"""
     left   right  up     down
00   0.0    0.0    0.0    0.0
01   0.0    0.0    0.0    0.0
10   0.0    0.0    0.0    0.0
11   0.0    0.0    0.0    0.0
20   0.0    0.0    0.0    0.0
21   0.0    0.0    0.0    0.0
"""

# 行為選擇功能
def choose_action(state, q_table):
    #state_actions = q_table.iloc[state, :]  # 選出這個 state 的所有 action 值
    #if True or (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # 非貪婪 or 或者這個位置尚未探索過
        #action_name = np.random.choice(ACTIONS)
    #else:
        #action_name = state_actions.argmax()    # 貪婪模式
    poll = q_table.loc[state, :].sum()  #設定獎池
    if poll == 0:                       #獎池為0代表這個state探索過(目前無功能)
        action_name = np.random.choice(ACTIONS)
    else:
        prize = random.uniform(0,poll)  #隨機抽數字
        for i in q_table:               #輪盤法，加權雖機抽出動作
            prize -= q_table.loc[state,i]
            if prize < 0:
                action_name = i
                break
    return action_name


def get_env_feedback(S, A):
    # This is how agent will interact with the environment
    S_ = S.copy()
    if A == 'right':   # move right
        S_[1] += 1
    elif A == 'left':  # move left
        S_[1] -= 1
    elif A == 'up':    # move up
        S_[0] -= 1
    elif A == 'down':  # move down
        S_[0] += 1

    if S_[0] < 0:
        S_[0] = 0
    if S_[0] >= N_STATES:
        S_[0] = N_STATES-1
    if S_[1] < 0:
        S_[1] = 0
    if S_[1] >= N_STATES:
        S_[1] = N_STATES-1
    if S_ == [N_STATES-1, N_STATES-1]:
        R = 1
        S_ = 'terminal'
    else:
        R = 0
    return S_, R

def update_env(S, episode, step_counter):
    # 視覺化探索過程
    env_list = [['- ']*(N_STATES) for _ in range(N_STATES)]   # '--o-------'
                                                              # '---------T'
    if S == 'terminal':
        env_list[-1][-1] = 'o '
        for i in range(N_STATES):
            print(''.join(env_list[i]))
        print("")
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        print("")
        STEP_ARRAY.append(step_counter)
        time.sleep(0.001)
    else:
        #interaction = ''.join(env_list)
        #print('\r{}'.format(interaction), end='')
        env_list[S[0]][S[1]] = 'o '
        env_list[-1][-1] = 'T '
        for i in range(N_STATES):
            print(''.join(env_list[i]))
        print("")
        time.sleep(FRESH_TIME)


def rl():
    q_table = build_q_table(N_STATES, ACTIONS)  # 初始 q table
    for episode in range(MAX_EPISODES):     # 回合
        step_counter = 0
        S = [0,0]   # 回合初始位置
        is_terminated = False   # 是否回合结束
        update_env(S, episode, step_counter)    # 畫面更新
        while not is_terminated:

            A = choose_action(str(S[0])+str(S[1]), q_table)   # 行為選擇
            S_, R = get_env_feedback(S, A)  # 執行動作，接收環境回饋
            q_predict = q_table.loc[str(S[0])+str(S[1]), A]   # 估算的(狀態-行為)值
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.loc[str(S_[0])+str(S_[1]), :].max()   #  實際的(狀態-行為)值 (回合沒有結束)
            else:
                q_target = R     #  實際的(狀態-行為)值 (回合结束)(到達目標點)
                is_terminated = True    # terminate this episode

            q_table.loc[str(S[0])+str(S[1]), A] += ALPHA * (q_target - q_predict)  #  q_table 更新
            S = S_  # 探索者移動到 state

            update_env(S, episode, step_counter+1)  # 環境更新

            step_counter += 1
    print(STEP_ARRAY)
    return q_table


if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)