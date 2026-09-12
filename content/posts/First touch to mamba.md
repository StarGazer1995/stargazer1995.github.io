---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBXQKTBQ%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T195153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDKtUfpTjWxik9yotvYfhlz32lyj5uhUIDFlnNoGPNFvAIgMxjlK4w6s18j8l%2FwMAy8ngM7wcTmenomfgtqkSv11ekqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDABgyxGQKYc3%2FswPJCrcA5%2Fw3Na3O49U2%2Ful025GsP%2FRn7iFGNxjo06796QzoV9gRe6WrNbabCyD7waLulT5RPVJ2PnsGIEVTs%2BxTohwIXVX8p6kMu4GtC3f4rqEqUywf79MoTrWWoauYmEK9gs%2FE4y6OmSdIqsySqKth8iES4BD3VqC9DF9StE7OoitQKcVnoa5aJUUGeEZsl%2BGAI8x6ywE0yWSHxZ74rv2PBIvnRvTBuVH4OUPXFtqVzuTPYCKVmSrijCHTOmR8Rsu1VFT%2BCefqRHS38jZQcVWTw0SM1X%2BXXBaSu7CL2cFka6nu%2FGMR5%2BDTlAoUBJGwKpqv%2FbSJZaklLYFimje6%2FnnxGt2Xqt3busI3Qohfdc2eVcZuivnYAKh0MxelArt%2FZUZuMorVQyZSuEQYNgb26lmDuV7sF7QrTKRZ5uY3sA1NjuP%2FjmOeIkjhltKLSHDEUjayXlHPc4YK5f4sciCdU%2F1YKOmYTZzGWO8Ry8fFamT%2FSmLxeaLXHnRRSx7fgo8GW56ypi9MBQ6VNpc3riGBcp0bbB%2FgXPrlCxeo%2B8Fsm0Q3sUt0IcR64mx0m3GGPITlHnLWVU5iyNnCxJ%2FTzakYfEijsF5EuMflEmtS3VKQq8VFREENq0fPwcdabZVfbdym2L1MLrHltUGOqUBYC9PtmgmHNkdNSTmh7UMhjXGAv9L5fS9BZKShoorg8QFoVAhjdsgnKsu%2FpRrY3HFyfb5RZRClaF%2Bf9FoqBwZbIazUK7p9JquottCkiyWMAGqq%2BdZM7eSMZ22VoA3LK7dh%2F7fdQFSMdHxEm7YPfEUjnys3m0DCkLMs1SGqj%2BM%2BU1HxkXNFeVl25DCVK2GUJdgOmu3C1jTg8%2Fhm0ladCdF30Xeprt5&X-Amz-Signature=02295f7b4a80a60bcc24ccebd2de6fa69edae67739170b71dd8695cb2fd7adef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
