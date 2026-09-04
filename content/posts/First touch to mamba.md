---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHMMROZQ%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T171405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIGyQULCNjtANIWgMuLmg3XFBaZgXAkdQ%2F%2FaGyH3v3CXqAiEA%2Bc6sdFw1%2F5FkNx3fDGci65Hl9BYN6Qri2rEiIUHoQ3QqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMmLZC2LlPBCg9%2BD6CrcA%2Fl0u%2FPYzhnf1lfSfJi4Kxh8YNaPHbJb1GIVyn5aPeOaqFYYhw%2FXn64pAf0GHLqqWzY0OKujLxzY%2Fs66gHzxIKOjuuOUbsBpV3soaXIfi6rhPJuCc2mvuEvnHboBVrPJ8K47rg25gGovizbpNboZ7ESC%2F3FmiYqOVY9EsZ5loPRqreYOe%2BlRM3nhRGFiu8mlRRHILB%2Ft73z5aAHKi8PtYVPxTDoEAGNj0pI14dGNnaRFrtbOfXWlVh9FZCnpgNoFWcQVvYB1Mu15Gxps40P5tsNc4HoANXYKknja6kAbrBp%2F1UUiNd%2F%2Fy9kHyxDp2eLNctdfiQHiDMRhN%2BdfvqDoHruC9CdqmWOKCJzgB42AZTuMnT1mtj7ctOLPLt1iksbtZaT%2FyJXyCqWEqeKEW3ub2nrNhTTkuhPc7%2BBGYo%2BtSpFagMA0%2BQ%2FP7yg2%2ByPBQed0NAFUEN8iZyg%2FPtjASPPBwhZ9KgigP6lwQgr%2F06ASv8O%2Biyre1Oe3r56lQSdw03dHZ3jIdAGJgLXFk2Dd5euDm4WHbRMhowyXBymNT1Q9KAzj7DdA8%2B5ZzppcVlImC4blV7jmiboK0asZDRuu2x071VYTyxjdoCNznDhfEUqBr50%2F94j6adJ1fSXJpN8tMNTz69QGOqUBsDF%2FXN61w82tIWWAm5Cgucg4WgTApVVwvt8ws7P9nSpd%2Bhw%2FpjZS%2FF2f2oAqMZhCYixGF8oesqOwsiVLZzG6ONftNs%2FAS81kwoBWDhcDq3NJKrc%2BTiY57B4DMH%2Bv7Mz0Wyhe2SLe2V9V0enn6jIQog4SamxDUgTPZMU0Nfk5uoGwxyXrpAkTlhMYO1N4l7nX8DcY7LsmTqjh9UJqFxkM52sUssSK&X-Amz-Signature=89d43d2c1dbf3e8691065aff73fed56d9b15e9d37390cb9cc99c912a7fc0ff99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
