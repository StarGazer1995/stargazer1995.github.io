---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OEM3HUW%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T150005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCICgi3%2BxIEdkEHG5OorPhsc5FU00qO6EMlCRbmy1c8Tj9AiEAwe%2FT4UdVyR2ib9B3BJWOaVps2vfoa2USfoqHU4VSgeMqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGL608IpPP1VuziF6yrcA5ZmZOHUC2IDbmXCNdCBhg6XRuWz0zj8%2BqYL1vCy2wnhjvewYH5WdixJlABxkodMHGqDEIBSb4sDmm603deceN06ZbOduIACfw8sRVqdBgweMC8dXZU0Ax0p7nsWU00egHoFRiC3QDvYh%2B1%2BF6lJorAttrTu1rLHUYZjSBKqkZC1JaZgR8K49ndr3%2BslHTkLnwBsun09ynvX5NwzvWs3AEx%2FvlpHrbfWWQIiFhMFUhlXcq8N5wg5ebXOtEvAU0j7E3w4BgSoZpbZShZNUIxqRuMLsn8%2FBu7M5eHURhnR%2Fn3xXTksJ1FEqh6VhTCdWhkQMV3RhSFyYPoIs8l7dgbDdBaJv56iRBL8NnYBxGjrkBffyArV6rBsQc1HIra3WlY0dIQWJ%2FZqDEevXxsITnRi8P1XCCLmDz207gBIZ%2F24MMdNDDyN4xWqaMHUE4JAMLgALNp82TCE8bEU0wblohYrF1dqyJI7GF4Q2p4EJFaNUCVY1MbzlNMSnkQbjS%2FiOp6PABExBxd8DeSLFvBH%2F1eDYl%2BroY2bnciYHcw8a3%2FA16jivRmm1m%2FS5dz2caz6%2F3dig4uynMWDwADu5MC%2FKMoocgoiZb5I%2Bsv7eB5x1NFz07YqNMd%2BB3AoMoDeUEx2MLeb99MGOqUBXX%2FC5CMUWGjXMGoZYvU33tIiJuHHAD329PMxsNIaJtlI0UPVAfUnklPNFksF2VoDAgMJcVUSSG4xT%2FDKhGpAwLzKCn2v%2FV4pXoc7WB%2FJ%2BuL4Po3JuoT5OsJJf7GTMqGgIYA4ABrBKvUTAbK2xgja1ba78lGbs5yQgLuwevLFZV21dvoclX%2BqIYEUw1rH2%2BTehYi9mLdjpoNvUpC5D4mnTuWnfePH&X-Amz-Signature=57ebbaf2b2295857a797a4fc46591c9c0608c7afc7e6ba56602fe26da8e6aea2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
