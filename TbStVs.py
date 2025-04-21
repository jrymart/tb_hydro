from terrainbento import BasicStVs
import numpy as np

class TbStVs(BasicStVs):

    def __init__(self, params):
        tb_params = {k: params[k] for k in params.keys() 
                     if k not in ['seed', 'output_fields']}
        self.model = BasicStVs.from_dict(tb_params)
        rng = np.random.default_rng(seed=int(params["seed"]))
        grid_noise= rng.random(self.model.grid.number_of_nodes)/10
        self.model.grid.at_node["topographic__elevation"] += grid_noise

    def run(self):
        self.model.run()

    def get_output(self):
        return {}
    
