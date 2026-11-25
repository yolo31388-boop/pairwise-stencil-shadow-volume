# pairwise-stencil-shadow-volume

## 领域

游戏、图形与多媒体

## 主题

模板阴影体积

## 说明

非流形清理、相机内外翻转与按光源清模板。

初始状态下 `graphics/stencil_shadow_volume.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
