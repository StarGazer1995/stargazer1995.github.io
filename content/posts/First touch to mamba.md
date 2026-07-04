---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IZQLFWX%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T014552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIQDXkb63CctyX2Gm46Thx92BLtD4Et56UV%2Bt2FEIhQ6%2BAQIgbuGmfOXV6ElvdUqikUPp1FAcMIVDfVO01JPiNCNumRwq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDAZxL7kaF7TB5tQK4ircA8envCzDWrpWAj%2BvNHotOy7m%2B5wRPbZnwKgdgkknut53dS7Dl43AJcnxzORdjM%2B1FO2U9KlddeMoX6Hrz4QTlkepLcYhXwiRS0VHJlxBDFVbT9Jtq6zlJ7TZEPSsf6zhtcT4tuWUBUn6UAVDKwlNJbQ7pGnPSK1nwdEFCwJG5IVwefSxnbRK77Ks2j0oEbC%2BB6llVEavQXKKo%2B3xaiB%2BJZDIjlXcCehq24PC0kprcYTZbnSYX7bS7V3JdhtLAL2PIC1zQscD7%2BD2CI%2BP2fkmCdaXp1NO0vbHHbdvAbbmvE%2FS2aD03LhzBsshdH2PDi%2FG2mImhBH7L9AKEd8TLdJ4Dp%2B7jfV0B%2BG38psLsDhyHfq1u68y7pbTngmU982fMNWFfpF9olvYgp8tclU55qpYCRkl%2BKG1Q%2Bnm8Udl39XskCVjzMNpHEqK3cw452FJVaiBD8DkWW9MXNnQ%2FXcJ4YSJASV91ggYLgGV00WMuyHAGMq4ii8xBj39leSkmc3gQ7XGUVleaegsGPmBNXopXz5tf7ltsmj%2FJeFOh50nmohBbvF9AR2Kymgrh6N%2BWEOpmylPHHDsg0XSeN654PnHxgvCYjNpFiXRCwUcwfUWL1O5nPX8Is5fw04EOmJB0I1jMJ64odIGOqUBNOWDPlFeU06Ztj2anvH8mNFGSEWFf9sSOjuu%2BNm8yN5YflayHLs8pKIcAXk4lr%2FGMKJlB%2FtigZ4vC%2BZsr7gi3IKmAxmG2TjbYirHJ%2BPy%2BawCYOnPBSfZOBP9z1NbGoNAqnGpgUsvG1J0movzjU%2FHRG6F2jiTM%2FdTvM5P%2FujpUkpGKXkxlBhcLvFNtw9LOO4ZpgJGyQy1DPZN4UFoNPM2wlM13zrT&X-Amz-Signature=1c200ada6f156a77684e6e999f17ebd74f158230fd9a0ad77817bd788e7bbc6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
