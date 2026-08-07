---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663F564CZB%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T123656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDrBXMQNrnUy3GUFpFIFdAqOQwtUX7T0XWJElw4HG1XLAiEA8h%2B32Vdft9mkbOC2mOWtsaz9Phq%2B4TclqrreWCxW8AIq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDAizVrqyE5FDWVYw1SrcAyBIFJ%2B02kiP%2FUzQn9%2F%2B4q3LVz6nt2O3MsHkW%2BXArO8KuHnWwTvkEqP9Px2heypx4tXJleYrvyBaaHcJNViSEVSfaPceaUNR1No2utwsyNoAb35jcFWID%2FK6LCMQjRDAWAzjrPn4tYu3pB66kbkoUUSGERRH81yPtiR1q%2BVODpmQURuqqK1DBYQnr0%2Fmn47dW1haHoibLzmigbuPHJhL0ChpIMHqhen6mc4cBO%2BlhKp0gHybTNkzRlZX2MM3QgVPbUbkAkZSk%2BDRIFHnjeu8eceudIzcu6GWGiD8K4bM42ArVX1ZJxlAcqmqNYPylg7m866VXFiLsGO1Peh2aQFEFG6k%2FXIqjwxN%2BZMcFlbA23SGTwKat6nwtm%2FqwDyQyFazorCplw2k13Sa%2BrD1ZUEiFXgl0WL64g7sWO0xbMMnzJ%2FuraofQfCq%2F8T8Vp2gmOTy2FpX5uivgCQNrswXyTUDFlDyBL1Yl2IbSOfQ3zjactdzHiWOeo6EBI%2BK4tbreOQFNaZ0%2B7EsV9I%2F4ye4NQ30%2BcG%2Fvv8VKVy8vl3xt7N4MyAjOLJmrr5GNPGtTz5dFFoLR0FwBfzqL24SuJVyU6GzBFhzJXsQ19AhrkfMLz7wkbn1zvSwXsAfoz6Xt5oEMM391tMGOqUBd%2FRrIP0JPRzA8E3jjWdAvAG0x2xEQCLz008vlVIPHhEhhvS4GZoesNCBeQVRQoiMZQTg2bkY8duvG9d%2FVsulVIrYI6AoEVZEGDVjNTpWlYLT7vfMmA2KNkqpYJIBYWrUdVDiHESCvDx1ANEhq86oVq%2FuJ4xFMDuQZPVLJumS8SI2FNxg%2Buka0qq%2BlonON0lBZnqEwsb%2BAVfMSabOLoZl5CGDJVhU&X-Amz-Signature=91e8f2fbcbfdc49728ef1b53a58adf8d787129452ce03209e2a47c96192f9a3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
