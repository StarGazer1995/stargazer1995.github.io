---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665A2VECP7%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T134613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIAhZ711Pu0LnVMdIde4KKtKm5NNzHPFOOuonyE15fuqHAiEAk%2BVwfiyKO1Vbuwze3%2FcImHu3R6spPcc2LV6s9UwSyEEq%2FwMIPRAAGgw2Mzc0MjMxODM4MDUiDE0uEhHRUBVLAC12nircA%2FpHD9A0K%2BGLBK4wVmbu4wh%2FJt5sn4uzd%2BBJa26f5nse3aYM93QMe8Wt99Nd0yk1bRKiQQ%2ByMUw7DI%2FaWkaW4A%2F2TOUb25hRIvaQwTDbCpywQ9g%2Bfdb1Iw89vUqbFADKaVSrCDzNjeYu4sJTowsfrQYtzgjsxmf3rPGMvbBrZAz%2FoJst4TrufTxUTYz14lKK3IO%2FI72aCWO%2Bf9cdMOG0Srd8Xjrj2JzNfVXfI0NuW2IfXvnJL6DBhQkEhveg2BGMZlhMY0oZlj1rNVDHzwXpPlh7s%2FbymrfE1cfjkxTWabrN40I26vntLqllTbaFox1cPhhw0aFyPVSd3409eaMxTr4bfsoLjwfAUgZdFimIPw7mAR0oLyh%2BVg0T52EPKLM1HqAwyfv9x9ENuF67nypGpE1qMklAl9GRGX%2FaCmi4reRmlNL0LTZPhPJbn8Wiyt8ipN9Ud%2BwgtcYi%2FHgsZwBK8vdkES%2F4ajbiB4QyQnR1MFGEC8Q8Ti7NlMPlhXr10Dz%2B%2FAu8rhQhwCRO6Dh0QibBKoUOm6MkbWxSUwINGdI%2BNgLXIvjsudc%2FTeiFNtheb7sUI4Ohb57q%2FlAmycyLeFBOU%2FGvT3SDhGvP9kgdwBWQN5bB0JQ7hYVSDVe%2F0ZHRMP3Z%2BtQGOqUBpdtP6yIWzTmpkklYkpYBenUt4kXW1Xv%2B1LkBpP4XStjWpnp12zhaVWppLiQVyk1MKLt2WmTY6CXbr%2FCxYcrowbGYVt2frPt1D5no4GHTEFWPwpPcQZtcWBk0iY4iZaHB1QnTYN8YXaZxSybpEDPB1pi2ci4helec2aYaxQlDtNE%2Fyo9BhBOqyLtaGjoBSEO7xpxrjFTkSeL5GrYd%2Faqia9pYb460&X-Amz-Signature=55c743f08074918d1c354b4f1777186d37f46747e5bb16071a834ae5fad85484&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
