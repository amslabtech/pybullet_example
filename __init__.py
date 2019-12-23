import gym
from gym.envs.registration import registry, make, spec


def register(id, *args, **kvargs):
  if id in registry.env_specs:
    return
  else:
    return gym.envs.registration.register(id, *args, **kvargs)


# ------------bullet-------------

register(
    id='CartPoleBulletEnv-v2',
    entry_point='pybullet_envs.bullet:CartPoleBulletEnv2',
    max_episode_steps=200,
    reward_threshold=190.0,
)



def getList():
  btenvs = ['- ' + spec.id for spec in gym.envs.registry.all() if spec.id.find('Bullet') >= 0]
  return btenvs
