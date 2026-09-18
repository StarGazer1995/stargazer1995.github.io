---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UNX3G2A%2F20260918%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260918T064908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJGMEQCIDAqM3XaNwvq1ITXo8IYBsk1PIwaQg9TzfyuS9asm6q3AiA%2FT831iYf49wwADZFFgA9T1Blov7pD4iGEw2hpADwCHir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMUYHnEVfPApk8Go%2FNKtwD6FUdQVi8GkyoaR7p%2FnvNa7ELO%2BAkoqMuUg3mxL3U2K14oIGI8qgq%2FHfs%2BbbqSpWtXO6MsG8A1JftrblNeg6iqSuoG8Ubucci1h7pEtT5zPPU40rARGOvfnHebvUUVIGBHPCJHFNP1TtWagYkiDnmu%2FNy95IdOVUSMNYIM1%2BLl1pSudY1lm9pEsxul36YN7dY95nUEywzY9Qy9BpuGT%2Buryg91vEeinNeAnL2jTSJKC%2F1uddBZ2rAwwF43RFtxC0mwn3l63r1SGFjs6wTJJRPA57MG6WzGOQFj6%2FySKXjZXZBuB3HM%2BY4BQYwOMGN%2F9x68DbgLBNhmS3g3nb7zSLuHmj3tfKhvPs%2FHGVdnWVKnY85Wdbw2CxAiC%2BcXc7yOLcrRXO0g0%2BUAajo9AI5tQO2TVNmBh0AWuCbVWMoQLcm1PLds4Sf19JcquXeOMJRqoa9iCHY8l%2Bqo%2B4B%2FoHzfV%2BOK0D5%2BAQyzEZpnPfHxUKDXQOsj%2FU3m0DB96WRrEuHw4Ydez45YXXt1RqoSLPEZSOrDi6mP%2BeAWGKdzaP0tqXUZuOxhz9i9YKBRoU18rORaEw1QFAOMruqldtkYkxCHzp5Y5SAWOX7IeaVYmVPtQFBu9autzggIDb7RtYazQIw4Pmy1QY6pgHkO5I4xqJhZx00mkcFmJKmat7gf2YJdKbI4h7Ht7DXQD%2BksQePhF%2BWuTrRaHaftvVkuY742kRveR9M4wd6EtDrv58JexcniUaVNepdAzAQpooMJtZNjG3e90YaA6732CrJRBPCo78zvSEn%2FRygdR7YEPIsE7GEuc3NO2BDIEWXNJyJKZuzghUsFittHrWTexTp6jASD2qalzRhQexnBifKBjXit2NF&X-Amz-Signature=0bb7d84070e10e8ac9b05dbd671f9799a3de560dab884f052e4975badd6800ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
