from tensordict import TensorDict
from metamaterial_rl_env import metamaterial
import torch

# environment of a 10-node crawler on flat terrain
env = metamaterial(
    num_envs=8,
    material_shape="crawler",
    num_particles=10,
    max_steps=1000,
    terrain_type="flat",
    render_mode="human"
)

# odd elasticity
def policy(tensordict):
    ko = -12
    obs = tensordict["agents", "observation"]
    act = ko * (obs[:,:,0] - obs[:,:,1])
    act = torch.clip(act, -9, 9) # action space limits
    return TensorDict(
        {
            "agents": TensorDict(
                {
                    "action": act
                },
                batch_size = tensordict["agents"].shape,
                device = "cpu"
            )
        },
        batch_size = tensordict.shape,
        device = "cpu"
    )

# reset env and render 1000 steps
td = env.reset()
for _ in range(1000):
    action = policy(td)
    td = env.step(action)["next"]
    env.render()