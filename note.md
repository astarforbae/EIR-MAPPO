## 运行

运行命令：

```python
python train.py --algo mappo_advt_belief --env smac --exp_name smac_test
```

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
