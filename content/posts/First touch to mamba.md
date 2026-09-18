---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TTTSKXG%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T200602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrJibBqJpnQMkxkNjf1%2BmKmn3v%2FQSInv5hWria5YghYQIgXE8wYnANHuNmhulWi4E%2B8iNLtx9xivh3RQaj8llO4FEq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDIIDYU7f4Plrpd8k9CrcA9P7Z0ACdyXVg1Te%2BpvTxfhPhyK5U94CpLgMn9%2BDVSSu6zA488gy%2BAXUR8XhGddiodyE6qgy4XddxODkUDUcUe1LrII4qmKAVtfJR%2FOzCtAAGy%2BIcOhXq9sh%2BQpImtrz4EviuFCPE4%2FnUEwUvuGo5sTvLH%2BNAOvnfpCk3QLSvIbKcNeS9xb%2FeNNJkew4ZQCfGX%2BeZUIDQPfDFJ404kYXuBl6u%2FYDFUsJlISpWuMCil%2BhB%2BLT1yYNsfZme2cPzcQFaRFIK5Bj3vrcQ6kaENUwNzVieq1Hm5ZvNS%2FR1Kb%2BNntm%2B6pNLgsdQzRcqWPV6gQe3vtTWe85UPx9vdpFjh05zF%2FWVyFHEcJGEWYCz878MTnW1G7qaa0UYSndMQ5N9ab1SgvD8SUbNPtNzZ%2FiXXSLmR1JCWsuw7GbljRUu4Fs3Emt2eOZ0hkG7lbCz%2FvBVFeZhaLk9AWDx4iJYmRH%2Bn3Nw82170BodSiJcipPCKOwmQnsBvw5eGMBQSD63gq6NBpiBDkI1dv6Di31WlHNqz%2FwH8OnELXJXeSE4p4fQy2xTcd0dVgIkGeOoxnP40N2%2F6U9nUtbdkJQkrZWWSikAXJuvqMayvuqxoZlTvhDwNE3j%2FK11F65Ucr0GhYRbbWdMLeFttUGOqUBsYkw9zZEssY%2Bmk0ITDJeBa9dNO5pcxPjlk54cqlJ849w1tFgRjjs81N7yGbN7XZQYvAlLCos9CGcB3rE81%2FInESEWXnId9tMntjx1K8V2YmuwbStyxq%2B43DCx9Bl9sztW%2FyVud286jBjD72lfbBoR3gCaWm%2FpFITeorqBrfXB991Q%2Ba69xbqkKNApIkpyYeUcux%2FGuC2u4k4vQtYVb%2FYMWuYpGDV&X-Amz-Signature=24218900cfdea95729cf53691cfd8652ce2c8956afa2b843fc8f9012efef21f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
