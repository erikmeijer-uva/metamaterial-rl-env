# metamaterial-rl-env
An active metamaterial locomotion simulation as a RL enviroment for the thesis 'Reinforcement Learning for Locomotion in Robotic Metamaterials'

### Installing

```
git clone https://github.com/erikmeijer-uva/metamaterial-rl-env.git
cd metamaterial-rl-env
pip install -e .
```

### Usage

This environment is implemented as followin the specs from the [TorchRL](https://docs.pytorch.org/rl/main/tutorials/torchrl_envs.html) library, so all actions and observations are tensors contained in [TensorDicts](https://docs.pytorch.org/tensordict/stable/index.html). You can instantiate an environment using:

```
from metamaterial_rl_env import metamaterial

env = metamaterial()
```
Optional arguments:
- **num_envs**: number of parallel envs, default 1
- **material_shape**: one of ["ring", "crawler"], default "ring"
- **num_particles**: size of the metamaterial, default 10
- **max_steps**: timesteps before an episode is terminated, default 1000
- **terrain_type**: one of ["flat", "mesh", "mesh_cycle"], default "flat". Flat terrain has a constant ground at y=0, Mesh lets you specify a mesh of one or more lines though terrain_settings. Mesh_cycle cycles through 3 different meshes over the parallel envs.
- **terrain_settings**: configures the mesh terrain. Can be a dictionary with a preset type and arguments (e.g. `{"type":"stairs", "steps":20}`) or just a preset type string (e.g. `"tunnel"`). For the Mesh_cycle terrain type, this is a list of 3 settings objects.
- **observation_func**: observation function, one of ["dth_tot", "dth_tot_plus_own", "dth_neighbours", "dth_neighbours_plus_own", "dth_neighbours_plus_thdot"]
- **render**: boolean to call self.render() automatically whenever env.step() is called, default False
- **window_width**: width of the rendered image in pixels, default 1000
- **window_height**: height of the rendered image in pixels, default 500
- **render_text_lines**: list of strings to overlay on the rendered image, default []

### Example

![](https://github.com/erikmeijer-uva/metamaterial-rl-env/blob/main/examples/nonreciprocity.png?raw=true)
An example for running an episode with a simple non-reciprocity policy can be found in `examples/nonreciprocity.py`.