---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZMKUWTB%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T145156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYOPxgAx3Zky9AISZ8I9NcLg5i5RJQbPtsSleF1Fvr4AiEA7IPbebu9HAMt1%2FW77mNAuQbNZINvOSbp181IrwYmGz8qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAEkY0R4XuaP7BAU6SrcA7B0sTDh5iAepm%2FTFvc2fW1yB4qoNikJVPJR%2BEOAUejyySePJjSX2gKZ5uurgEHMuRpDaM4izFvL1wSg5fvd5DFvBoc6lNy6u7LW83x4dbf32%2BaN2Xm8dxo%2BYyh6HxJbAisf1qiOmBmPLt8O5xOytTbdwJLsm%2FRYgNww2MEC5WHIwzo0nXFH7IzHfyei2mlMwJ9LlNxva8H7t8aHad6UzQO13%2FoqApLQ2%2FwXCa92AY%2Fm9WXno3thKj13yxtxzszDKOLsILUzOyrSHKp8hNg1Rz%2F4%2F4izIb1NC%2FMLGBmeZ%2BHKELpPYFdzVlbX1rh1z7aCHelTOsttgtZpVlBj39pL2sfTk1FRNpX%2FqlOo%2BoBmutvOkXEBSi0brkFItwp%2BsKEJDfyMLL6qv2okXSmGpXEEscQEaVnM01IGjrfATxvo4tGSq%2FaXe1iscHAmACkdOOWxhJmHJ9fuQXyMe3ChHsYdwEjd7n1lv0mzrvlVS0p0AqMgNE5jORJEZ%2Fcd%2FELWwgYe4SB9ZgFlFbcP2jsic0W4igB9teN%2F6QjXnPpyMB4sVEA2Nl5nTBJ8SbP4tmTa1s0NANVS%2BYmlXNfwvjbEG6ul910G7Exd05Jx%2BPajsdkOPUwQr87LsqcFWVH%2F%2F9LlMOHx29AGOqUBu9XV5zcrH4JrFPA%2Ba71lKF5PHqBZMGnWBJ8fniIwd9tr%2BtTNpePtJihPRO5fiymYMpGmciahoOSs7yq1Iz8bPAyScZj8b3VVbfE%2FQ8U1gPPfxZSQwaJMh7mk4H%2F%2Be0kHktPrbWMi6M6Id4wxNukepF6Sihww%2BDg3agzn3Y9b7uV51asvnmxyiAXVQF91yDruCqTucAXcPuRcRac%2Basz1493rLJqt&X-Amz-Signature=8df1b91f4a3eadc71a6f386ef1006f6baffc66fcb3f738bcf15d95f02faca9df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
