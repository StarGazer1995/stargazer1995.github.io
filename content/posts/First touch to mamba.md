---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6SUZED4%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T222941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCQ%2FdVPuvCTFf4ud7vHYRoZKEAAzFDQIn0rAbjYvYKOOgIgRzQWyGMQnH0J991XJKdgm1SNpzn55%2BY%2Fm1xK7tsU4Vkq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDOpimRme08dAjaob%2BSrcA6vHGC7Po15aFGGOnPmxa%2BuBBPX7WcjisHpgBLx2JZCHmIrCqKRw%2F3xALbHCK0fZfTgHSC3eP%2BhreDy6WDglLH1jJE53oWGseNfnlgY4202cHLzo9wIWlq%2BhXLrHZM5XimB%2Bz4Ewrtotpy29dUD%2B5oOTb8hKT4%2Fb16jXTFaWm4JNxD4DHAY7gC01izueCYog%2Fg45N1SIBpqZX6NdLu%2BwTLvAmGd%2BDT9ghBu8I1%2FDxWICRsEHE6eiAzgx6heniWJPehMUg3Slw4hEXCbdMxMlMaWrWNtWaG%2BLgbsGDaeQNLd5p4yZ2TTs1E9tWHw%2BO3M%2BJSIr4nIW8yqx1cWWXCvxB1n1ZzReAAdcqJ%2BBgj2pO7ttJQPSK%2BZWLca17HlXSy3eFJU9JJzmM%2FHa0b3%2BzPMHM%2FH5xTHg6PkcggeJIjaV0fRCfJTOKPE3erm68KGBAmRmtaNGPuamfxaf39Nu79yBx9sQHeF5dC22zPYyKTKuBI0tGBclvkhcybQ2J9UOhsKhCssWCsC%2B%2FLMHaXjW%2BM56Y20wDVe4pC3gmA%2FeGTJBkDeo4gx2b73%2B9X2U4VwWBu%2FrD00jTi2Sw%2FubERPz732g3%2B7MG7XBxSApJHljPjhk9FEZbznw9n%2Bze2LbMBKgMLK%2BktQGOqUBjzydexa4GA6vXc%2BEWVwe3PNIoNF%2Bl%2FmyqqNjH4d5Efg33xTlT8w1up53zSFJWT2kMjDxwkR7gtYtmuTxXu9%2FDMVxC212Hu%2Fh2uuuf5b7MF5E7gwPUuf3C291wzAtx1QtmcLULyH3Fo6YyHoLq9ax8R8xm5ai%2B%2FQf6TjtbvZwek6%2B1dTHZ%2B%2Bo%2Fajvg0FofTX9ZixdSuFRBhu7220chV5nL%2BoJ%2BEGg&X-Amz-Signature=9c36bb3fb380f9e0b4c56305d339207c6dc1a924c88448f05dd256d215f14b7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
