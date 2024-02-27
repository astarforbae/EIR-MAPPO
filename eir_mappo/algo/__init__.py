from eir_mappo.algo.mappo_traitor_belief import MAPPOTraitorBelief
from eir_mappo.algo.mappo_advt_with_belief import MAPPOAdvtBelief

ALGO_REGISTRY = {
    "mappo_advt_belief": MAPPOAdvtBelief,
    "mappo_traitor_belief": MAPPOTraitorBelief,
}
