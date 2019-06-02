import os, subprocess, time, signal
import gym
from gym import error, spaces
from gym import utils
from gym.utils import seeding
from gym.envs.mujoco import mujoco_env
import numpy as np

class HersawEnv(mujoco_env.MujocoEnv, utils.EzPickle):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    mujoco_env.MujocoEnv.__init__(self, 'half_cheetah.xml', 5)
    utils.EzPickle.__init__(self)

  def step(self, action):
    ...
  def reset(self):
    ...
  def render(self, mode='human'):
    ...
  def close(self):
    ...