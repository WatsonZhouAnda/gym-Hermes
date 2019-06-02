from gym.envs.registration import register



register(
    id='Hersaw-v0',
    max_episode_steps=1000,
    reward_threshold=4000,
    entry_point='gym.env:HersawEnv',
)
