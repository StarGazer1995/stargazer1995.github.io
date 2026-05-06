---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3TP2DIW%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T114417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpP5RpXEViaAecX4cPO9Bh8RntK37OhhY7msnUKzugMgIgQ1773g484s30QNDyWTXUJJMtJLyt77hphxTw%2FnlexuwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPwy7WthhISADrpcCyrcA6L28UKMeZFxqSlwl7o6Eetadmt6IdfJuNwC1O8ygy0Nm2nOxfUPXEL%2Fzb%2F9GIzC%2BFb0yc0Egf2Mr4lWMmU69R1X6saX2%2FYwyWWn%2B0%2FHHJNt3znv%2B5WctwJnK08G%2BjWBW03CFROj8u%2BaXzTW%2FFrcRoV8u2q69DlKLPQt8os2mrVjmpb4iyKrPTkxDG6IAtwfb9uxLBtiupoL6i%2ByC42p9AVX7aZ2iLGkmgOYkbhyvhm8mCYVc3n9ivFoEjPvoivB26p2GUGCYAs9FfxTuRe3eoHyokaSVEnTYaeCK3wyl5wzS8A8chfJUDETfEkSo5cryBohkC9DVZtmXjuMteoIS2S5ZdO9JCzc%2FQl6eWgqi%2B1dOVQmWSfzH8qcRxyahm1xZZ9e8S9r%2B%2BS2O2gZ7M50EwmVr0NZX%2FJ1IBUZ05SMok3c4KfsI7xmGID1guxRvIruxzPo1QTm%2FLKtZ9DoRQitP9OEBBFIWnU9iHT9IMzSR7zyvFXo8RE3dXzFp75AK0ML37uj%2B4%2FkBHDyH0uCdZkj2cqm1FCCCW%2FlD0DIva%2ByeDu1VdqOQ9%2B4TUu6BV4vLzb1HDlOJmMNvsOfabtzz6Zk1n%2Bpirb%2BsVNn9wTuGOFQ4sm9P4X1YTl62Ei0CG3DMJLH7M8GOqUBJM4QMObP29UjPeCZmr93EZiuvQq1x1up4NT16nDMp3uoVjNeBY7rMdS8Ep%2FQUJsACPuNQ%2FwtlEP6Vu7IhNKvtD2eaTGht%2Fj9OyXmAJNSCgzk9caDZ2X3Oiwc4FMOorM%2BzDeLs8HAqVhkMTzB5oAvZgDszOaSfkXO39peJHAIu0i0oW%2BnMIN7FEFKpxMBT5AeiyXw%2BVR%2BUabwuOvEVTO7%2F6HJqJ%2Br&X-Amz-Signature=2dfa232c8af71e08805c4529515d9f50f8083e6f749502b9959143e53c8d5242&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
