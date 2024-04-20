## 运行

运行命令：
`origin`

```python
python train.py --algo mappo_advt_belief --env smac --exp_name smac_test
```

`5m_vs_3m`

```python
python train.py --algo mappo_advt_belief --env smac_5m_vs_3m --exp_name smac_5m_vs_3m_400w
```

`7m_vs_5m`
```python
python train.py --algo mappo_advt_belief --env smac_7m_vs_5m --exp_name smac_7m_vs_5m_400w
```

## 实验结果

### Origin

#### 2024-4-20

`settings`:

1. `4m_vs_3m`
2. `episodes_timestep` 4000000
3. 结果: /home/ZhangXingYi/codes/EIR-MAPPO/eir_mappo/results/smac/4m_vs_3m/mappo_advt_belief/smac_test/1/run7

### 5m_vs_3m

#### 2024-4-20

`settings`:

1. `5m_vs_3m`
2. `episodes_timestep` 4000000
3. 结果: /home/ZhangXingYi/codes/EIR-MAPPO/eir_mappo/results/smac_5m_vs_3m/5m_vs_3m/mappo_advt_belief/smac_5m_vs_3m_400w/1/run9

## 笔记

环境：`ShareDummyVecEnv([StarCraft2Env()])` in util.py

1. `actor` 一个智能体一个 MAPPOAdvtBelief
2. `critic` 一个全局的 VCritic

## TODO

- [x] 调整Team中agent的个数
  1. Map Editor：顶部菜单栏Modules > Triggers > Spawn Marines中可以看到个数
- [x] 控制打开的窗口数量
  1. 可以把use_eval设为False，不过不太明白这里的eval是干什么..
  2. `mappo_advt_belief.yaml`中train.n_rollout_threads个数应该就是窗口个数
  3. `mappo_advt_belief.yaml`中evel.n_rollout_threads个数应该就是窗口个数
- [ ] 控制`adversary`的个数
