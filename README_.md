# Byzantine Robust Cooperative Multi-Agent Reinforcement Learning as a Bayesian Game

## Overview

This repository is the official PyTorch implemetation of paper "Byzantine Robust Cooperative Multi-Agent Reinforcement Learning as a Bayesian Game".

## Installation

### Prerequisites

- Python >= 3.6

- PyTorch >= 1.8

### Install requirements

```shell
pip install -r requirements.txt
```

### Install StarCraftII

Please follow [the official instructions](https://github.com/oxwhirl/smac) to install SMAC. Our experiments are conducted on **SC2 version 4.10**.

## Usage

### Training EIR-MAPPO

```shell
python train.py --algo mappo_advt_belief --env <smac|toy|lbforaging> --exp_name <exp_name> --obs_agent_adversary True
python train.py --algo mappo_advt_belief --env smac --exp_name test1 --obs_agent_adversary True
```

The default settings are in `eir_mappo/configs/algo` and `eir_mappo/configs/env`. The trained checkpoints and tensorboard logs are saved in `eir_mappo/results`.

### Train adversarial policies

After training the victim agents, you can load the checkpoints into the network, and train for adversarial policies.

```
python train.py --algo mappo_traitor_belief --env <smac|toy|lbforaging> --exp_name <exp_name> --obs_agent_adversary True --model_dir <path/to/your/victim/checkpoints>
```

## Reference

[PKU-MARL/HARL Toolbox](https://github.com/PKU-MARL/HARL)
[On Policy](https://github.com/marlbenchmark/on-policy)
[Oxwhirl/FACMAC](https://github.com/oxwhirl/facmac)
