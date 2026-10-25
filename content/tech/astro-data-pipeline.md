---
title: M16 拍了三批，十月那批我没并进去
date: 2026-10-18T10:30:00+08:00
source: local
series: 天文摄影
description: 六月一个晚上拍了两张，十月又补了 50 分钟，最后只有六月那两张进了成片。
tags: ["深空笔记", "天文摄影", "PixInsight", "数据处理"]
---

三批数据里，六月那两张是主力：一张给构图和颜色，一张给细节。十月这批是后来补的，没通过检查，留在硬盘上当 Hα 素材。

最后的成片是六月的构图，加上细致图里通过检查的那部分高频。

## 三批数据

六月广域是一整片星场，鹰状星云在画面中间占一小块。ASI2600MC Air，280 mm，2.77″/px，NoFilter，9 张 300 秒，视场 4.79° × 3.20°。

![六月的 M16 广域](/images/astro/m16-wide.jpg)

*2026-06-06，ASI2600MC Air，2.77″/px，4.79° × 3.20°*

六月细致图是同一个晚上的另一台镜子：ATR2600C，414.7 mm，1.87″/px，HO 双窄带，视场 3.22° × 2.10°。星云填满了画面，代价是窄带把恒星压掉了九成多，噪声也更大。

![六月的 M16 HO 细致图](/images/astro/m16-detail.jpg)

*同一晚，ATR2600C，1.87″/px，3.22° × 2.10°*

十月那批还是 ASI2600MC Air、280 mm，10 张 300 秒，和六月广域完全同一个像素尺度。

![十月的 M16 HO 单批叠加](/images/astro/m16-oct.jpg)

*2026-10-07，10 张 300 秒；ABE 去背景、校色之后的线性 master，再按 STF 拉伸*

三批直接倒进一次叠加，广域的构图会被另外两批的噪声拉走。我的做法是先各自 stack 成 master，再一批一批地比。

## 怎么判断一批数据能不能用

新数据进来，我先不看它好不好看，按顺序看三样：能不能对齐、能不能提高分辨率、高频是不是真的。三样都通过，才考虑并进去。

**配准。** 用星点做 Hough 匹配，先估尺度、旋转和平移，再用最小二乘精修。十月那批对广域：尺度 1.00007、旋转 +1.042°、平移 (439.2, 4.5) px，717 对星点，RMS 0.368 px。它不是纯平移，还带 1° 旋转，不 warp 直接叠，高频相关度是 0；warp 之后是 0.54。

**分辨率和噪声。** 像素尺度决定分辨率的上限，FWHM 决定实际的锐度。十月这批 FWHM 4.99 px，成片 5.16 px，基本一样；单位像素噪声 0.00029，成片 0.00013。尺度和锐度都跟成片一样，它提不了分辨率；噪声更大，并进去会把噪声也带进来。噪声不是平场或堆叠的问题：背景比成片亮 2.5 倍（0.0214 对 0.0087），帧数还少，是光子噪声的极限。

**高频的真假。** 找一张同网格、深、低噪、结构确定的 starless 当标尺，在星云区算高频相关度。相关度高，说明高频跟着真结构走；低，说明主要是噪声。六月广域的 starless 就是这张标尺。6 px 尺度上，成片的高频 89% 是真结构，十月这批只有 40%：

| 高频尺度 | 十月 HO | 对照：成片 |
|---|---|---|
| 3 px | 0.12 | 0.83 |
| 6 px | **0.40** | **0.89** |
| 12 px | 0.68 | 0.95 |

3 px 尺度只剩 0.12，12 px 以下都不可用，所以不并入。

真正把细节提上去的是六月那张 1.87″/px 的细致图。合成之后，星云高频和它的相关度 0.998，原广域只有 0.695。

同一套判断也用在 NGC 7380 上：13 个晚上的数据最后只叠了 11 晚，哪两晚不要，看完每晚的 master 再定。

## 合成时只换高频

通过检查的数据，只替换 6px 以下的高频。处理在线性域完成，先用 SXT 分离星点和星云。

```
$T + mask_overlap * ( B_starless - gconv(B_starless, 6) - ( $T - gconv($T, 6) ) )
```

`$T` 是基准图的 starless 工作副本，`B_starless` 是新数据的 starless。6px 以上的低频全部来自基准图，构图、背景和颜色保持不变。合回时只用基准图自己的星点——细致图是窄带，星点对比度只有广域的 8%，不先分离就替换高频，星点会被抹掉一大半。

`mask_overlap` 从新数据的数据边界向内收缩，再平滑。配准后的边界外是精确的 0，`gconv` 的零填充会在边界内侧抬高一圈高频，拉伸后就是一条亮边。

## 流水线

| 阶段 | 入口 | 做什么 |
|---|---|---|
| 0 校准帧归档 | `calib_ingest.py` | 按相机、温度、滤镜、场次收进 NAS 校准库，生成 `calibration_paths.json` |
| 1 准备 | `pipeline_prepare.py` | 读 FITS 头 / RAW EXIF，按夜晚和指向分组 |
| 2 单批叠加 | `run_all_seestar_nights.sh` / `run_wbpp_target.sh` | 每一晚或每一批单独 WBPP |
| 3 质量判断 | 人看 master + 数值测试 | 决定这一批进不进最终图，以什么方式进 |
| 4 叠加或合成 | WBPP / `pipeline_union_pair.js` + `pipeline_finish.js` | 多晚同目标做总叠加，视场不够做 mosaic，多来源做高频替换 |
| 5 校准 | `pipeline_correct.js` | SPFC 流量校准，可选 MGC |
| 6 校色 | `pipeline_spcc.js` | SPCC 分光光度校色 |
| 7 预览 | `pipeline_preview.js` | 自动拉伸、导出 JPEG、归档 |

单次目标叠加：

```bash
./run_wbpp_target.sh \
  "$HOME/nas/media/activities/2026-06-06" \
  m16_wide_20260606 \
  --calib-json "$HOME/nas/media/activities/2026-06-06/calibration_paths.json"
```

帧数超过 140 时分块：

```bash
./run_wbpp_chunked.sh <src_dir> <work_name> --chunk-size 140
```

mosaic 只在视场装不下目标时使用。IC 5070 的 Seestar 视场是 1.29° × 0.72°，3553 帧、5 个晚上、6 个指向，按指向聚成 3 组，各自叠加，再拼到一张并集画布上。数据仍然来自同一台相机。

## 代码

这套脚本已经脱敏，放在文章下面，MIT 许可。

完整目录和说明：[README](/code/astro-pipeline/README.md) · [下载全部（zip）](/code/astro-pipeline.zip)

主要文件：

- [calib_ingest.py](/code/astro-pipeline/calib_ingest.py)：校准帧归档
- [pipeline_prepare.py](/code/astro-pipeline/pipeline_prepare.py)：按夜晚和指向分组
- [run_all_seestar_nights.sh](/code/astro-pipeline/run_all_seestar_nights.sh)：逐夜 WBPP
- [run_wbpp_target.sh](/code/astro-pipeline/run_wbpp_target.sh)：单目标 WBPP
- [pipeline_correct.js](/code/astro-pipeline/pipeline_correct.js)：SPFC / MGC
- [pipeline_spcc.js](/code/astro-pipeline/pipeline_spcc.js)：SPCC 校色
- [pipeline_preview.js](/code/astro-pipeline/pipeline_preview.js)：拉伸和预览

所有绝对路径都换成了 `$HOME` 或环境变量。`SEESTAR_WORK_ROOT`、`SEESTAR_NAS_ACTIVITIES`、`SEESTAR_TARGET_DIR`、`MARS_DATA_DIR` 按自己的目录设置。

脚本按原样提供，不保证适配所有相机和所有数据。

## 数据放在哪

原始帧按夜归档：`activities/<夜>/Light/`、`Flat/`、`Dark/`、`Bias/`。校准帧单独集中：

```
calibration/
└── ZWO_ASI2600MC_Air/
    ├── Dark/set-10C/<场次>/
    ├── Flat/Ha/<场次>/
    └── Flat/NoFilter/<场次>/
```

温度看 FITS 头里的 `SET-TEMP`。历史目录里写着 `_5_degree` 的那批，实际是 -10°C。

本地只保留正在跑的那一份。有一次清掉 130 GB 中间文件，根分区从 148 GB 可用回到 278 GB。跑完确认 NAS 上有 master 和预览，删除本地目录。原始光帧留在 NAS。

## 踩过的坑

**FITS 的字节序和符号。** FITS 是大端存储，16 位数据是有符号 int16，物理值要加 `BZERO`。用 `<u2` 读，图像看起来平滑，也有 RGGB 图案，绝对电平和通道比例全错。数据偏移按 `END` 卡向上取整到 2880 的整数倍，每个文件可能不一样。

读错字节那次，我同时怀疑平场、WBPP 校色和窄带数据。后来改用 PixInsight 的 `ImageStatistics`（Normalized Real 模式看 median）读数，问题很快定位。

**窄带的 plate solve。** Hα / OIII 星点稀疏，WBPP 会报 `Unable to find an initial linear transformation`，master 拿不到 `PCL:AstrometricSolution`。事后单独跑 `ImageSolver`，用 master 头里的 `RA/DEC` 和已知像素尺度当种子。

**PixInsight 的实例槽位。** GUI 占槽位 1，无头进程落到槽位 2，星表会“消失”。跑批之前先关掉 GUI。

**`FILTER` 关键字。** ASIAIR 不一定写 `FILTER`，WBPP 默认标成 `NoFilter`。correct 阶段显式传 `--filter` 和 `--filter-nm`。

## 验收

看产物，不看退出码。

- master 有 WCS：`hasAstrometricSolution=true`
- SPCC 打印通道缩放，例如 `0.0623 / 0.0616 / 0.0622`
- 多来源合成时，成片星云高频与真结构标尺的相关度高于原图
- 配准后星点最近邻偏移中位接近 0

SPCC 依赖 Gaia DR3/SP，MGC 依赖 MARS DR1。星表路径配置不对，脚本也会跑完，结果不对。

## 最后

脚本负责把每一批数据做成可以比较的东西，决定哪一批进最终成品的是人。

M16 最后的成片，是六月的构图，加上六月细致图里通过检查的那部分高频。十月那 50 分钟留在硬盘上，没有并进去。
