---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677Q5CXBO%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T051929Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDagNxzDeez3e7EVVSoGfG%2BBy8%2B5%2BSzakTVfMChvHTuwIgEKLhdo%2F24JcPk77Jsp7PiSHdtxWVqfHILCM0yQJjuQQqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAQjzBlRlelvQYhnEyrcAziLtL%2FuIAWn6Vy0RDIGI9sqGpo09lD0x90B63ahB3C029zYNXavmY3uDlg%2BLUMm3rMXaY4NF908DOePl3NgDfDkQh4mpzVL1n7CQ8VoE0%2Bjj2Xytn3aBc1x5l1R7ZCsQk1s3EiwouH9cs9SYZIzsUdZu3I2j6qxJqubeoPZK%2FZdtaWpZpYf%2BDam6TkAsWQbfQOnqNC0MowKkS7xXYdGgIfg6jw9FtmIebmc%2FmMbUIP453ZxQa7VjJMAaPsvc5GXsGOxMISv7ghDLmyIhCQwOrInJ2zLpYtGznmgaAtosWXPLhYc%2F%2F28ergO2Iymk2Ap6pnr76xlusUQChf0rHB7nm29WYazK%2B%2FTCs%2FQLCBlb2ovQftYOs%2Bck5hTW4xLwv5D2tFZmwta2ljiEijEajxZx%2F58GOqQ%2BXpGL144%2F3DjpD%2FhN5laGVB4Ck%2BYEiKGitcy%2FdMDo3%2F1IsxAvA0z5QDRdCl0qEhvptuSeHjnvai3TBj9P3hB2jxQ63kDjJq20AAxXGM7Q%2B1bQgHG%2BUh6yiuiW99U4Vk5wirmOCwx5VW7B6MKjC0uC%2FSdiJJzYQ9lU79Re4ZF39y%2BoivNciGc92NHqdwlHdaTxhXP2PulaZt9bEcJ%2BGLimSaGG3fUoP8VMLuY688GOqUBC8znrZWJ4L3xFONEjyrG7XQQ8smp9VPWZRDzfvg9neky4fELqo50EtGy2nNlc02kfpyFhKyhgoP%2By%2BRr8ybUHxYeFTCwHdHtNvtdz4h78Y8uqEZ5Ogt9%2Bcj9FMUhgygGNOEWGT8fwTaoaLt1CbCl%2FVcnZu9mrhaFFA1iwC5rykKsvSM0sfJGc8mFQFGwI2E41WqL39sSuN6gE4wBbXJfQ2haSBgk&X-Amz-Signature=cbb9529f9f9247973569d2ab668cfacaebcba623997984fc2063855140be149c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
