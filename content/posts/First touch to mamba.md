---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JO2YIW2%2F20260505%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260505T233409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChlH4AipMgjMbdX%2Bs2H7%2FUFyf4p3JBSTOVFoU%2BdT5dxAIgRhRX2lI6ThcfdtyVz6h%2BvFmDhQHE3U4iZGw%2FIimeK38qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN5kIS0%2BLSpNtzxxoCrcA1PgqyzvOQfPPk%2BtpNNMipsT2gDntjZBSAcuFigKTQmT0m9p9ouL5eHO0n6QvYpNXYGRoxadXrxUHS6XvIa5WIZIYDvOp8kDyMLmKNK6j8Mxv3n85N5JhK0JYrVVAWu6dHrcJNnT%2BJw%2BeaBcJIwLlok4qWHViyEW0Nty2MkVl00Tiinoqo8eEZWVPLuRUhVtNaLw0XzNzPAei5QLJgtyBI67z4Yf9%2FiMopn7odimXTgiQamdXGeQQz2avNtQP2wG2O%2ByYgIoqCLsTrUtm7oLIIkeqmqzz7PEI5TXk1OvqFxx5bV30nLmpKFYsIB4WrBzuBhtxjRSD2dztwFW1o5hHW8LkNkw3UbHvybjUaGZMTp6pjfV4%2FEXxn7K5hrPhG1xqkVAXr60FqYfVlR1DxNR37PtoDv4a4xtIZT9cROziPl6z5%2B48oMNktziSdutXqp4sub71Gw8bTO2Pnji4O1ebmJOvwFw1fPWyh09DjwzSGhKtTrSnpaP2K55Hbp4n88e3RpOibbTrE1DbrsJfje5bxYRBINiLvUbI13BmvN278Gdz2yy5CqalOb0%2FnUuQQXZe8jO4SIeZBQVA3sWFYVBT51w%2BF3UVPnpDO7uRkq9dT4YXHAYx2wWb0SPvvD%2FMIro6M8GOqUBrc8C0ounUOS3OI%2BP%2FPFY9GfMxIzEsnsFy88qwHYc7UqEFSgsv02d%2FzrK9NSsy7YBqzAcFmr%2BY6XcUaO%2BdPHlCB9xZLqhW0n4y%2FdrCCT4NVLO9khBEv9EWSivipBqaypC96ThR6C4pf1tpurmIMlJqNN8dd2c1129JjXYS23wl7p7FuPg0jdZq9kzaKfPU51CU0H0DMEE8eQngDxA93LZhEM%2BGo%2Bl&X-Amz-Signature=c89ab63cbc237a17d15cd4f431e7e490e857046baffb522236583117e525884b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
