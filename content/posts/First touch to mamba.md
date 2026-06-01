---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JSYPRLW%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T154738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCID6dVRYmwXim%2BxXR%2FolD6YxSeRxc%2F%2BhGWVfjqeizmgB8AiAwV1kDm4HNztn4qxo7V30fJJrKCmEMJJmpoO2pmnd9Oir%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMrCNg2sn6ic5ZJyPVKtwDZReemYjwKlqnADf11%2BxL13Vq2KwpwTnFONxugzy5PfUfdXZtYolArWsH55%2BTuwQp1S9LTcZvAPV1SNtzTAS%2FR1jDGwFor4cNeCt5O%2BQ%2FCbfaTgRuxduo78wTlWZUGw1JTjP2g8fN7gyPW1Hz2ogd%2BRStrzTY27cz22RRkXSQUgr%2BYBhOS9Xysrh12zBq9yEXKquSbNWMplWaddmd5Xyqj00YoPi1pOTUm83gnyaqOxhPK%2FnNx0BAgXbhHsc1fe0TTHinglx9r44t4I1m%2FpmDKQ9ZIM29FwV5tSpveDPhLpGDRhV%2FOZ2OwN4k4ZG%2F%2B2S4HbFBSsHHNApc4rpMgw3MgisNhoIBYyuLk02oFbZohYC2enLvjH2HSZQFXlFn0nRTLM%2BM%2F92kjv49v9cXPiK0UvVQdMbtX5ltTsRMbw8dszsw7XQg3hc0tDQcaeSplEFvWQUqMcyV%2B755B95KrO7sP%2FT7ZGtDhx2GMmMXREKZAigPnFNBuuymeA2fYSkChPOtiMBfcfNWHhVTu2%2F14WFPHt%2FdY8wSYEepxpupdzs7Hu3o5bqpbSrVMJX615kBwi2tCJoxsUmcDZfIMjiMjubqJcf84W%2Fgtk1NjazBevor8YHpPx%2Ba5f%2BwE7rbAKUwnrf20AY6pgHsukQbzUPw4hhELMCssxbQQ0uIamqfj9eGOUlYwx%2BfqoRdQtF%2FY1n%2FZPKQzl6bAM%2Be%2BEeqjExci8grGjdHedyobsRLPZSgChY5JiqtBLG5QDOlcGVP%2BVHI7fGLEaen8yOdbBNtfxduvlZwMcZV%2FgXotned1PhFv%2FisLabrESl6uMSYxYOfGPuCBzPKzqtGtBH6cO2PkxQt8XFnR0klXmm7urrKzgWV&X-Amz-Signature=164fbcdd9c852e9337499b0d6cc69a34d48258536c38cbbef1ef1c958e4dfdb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
