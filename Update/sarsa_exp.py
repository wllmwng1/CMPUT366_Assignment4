#!/usr/bin/env python

"""
  Author: Adam White, Matthew Schlegel, Mohammad M. Ajallooeian, Andrew
  Jacobsen, Victor Silva, Sina Ghiassian
  Purpose: Implementation of the interaction between the Gambler's problem environment
  and the Monte Carlon agent using RL_glue.
  For use in the Reinforcement Learning course, Fall 2017, University of Alberta

"""

from rl_glue import *  # Required for RL-Glue
RLGlue("gambler_env", "mc_agent")

import numpy as np
import pickle

if __name__ == "__main__":
    num_episodes = 8000
    max_steps = 10000

    num_runs = 10
    data = []
    for run in range(num_runs):
        RL_init()
        episodes = 0
        steps = 0
        RL_start()
        while steps < max_steps:
            rl_step_result = RL_step()
            is_terminal = rl_step_result['isTerminal']
            if is_terminal:
                episodes += 1
                RL_start()
            steps += 1
            data.append((steps,episodes))
print(data)
