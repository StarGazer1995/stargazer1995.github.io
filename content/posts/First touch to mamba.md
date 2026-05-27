---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXMNLATR%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T214434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9xpkMYpR8Zeus%2BcMbV9W1J4Fwj%2FtGyMuEMdDsU7yvnwIgd%2Fvg5FntsAVd%2FVtu8Q0Ha3KyFZ%2Br7vN3s%2BLcPOWZQi0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEXyfi0hMfvXe8dGCrcA7bG6ucCyhsJ%2FsJhW7OhjmTNGyh9Y55HjRYKzth0koMqjF%2BlWQKU%2BeHNNs0eMeq9%2F1eWZl0r1nEX3lkjJ1apoBE1YUYsqDISNyBVfwUhsmjmGu%2FuEqtAS%2B9McltpBrYozpvPvzS0vvcitLxzB%2BuYSE6nyKAPR4c0YrAkmLzs3P0ci9KmRB4etRfoqKbhZpAErBb7%2ByObht06u8K3RsiT13uyyXS%2FJgllgC51tQsJjqHFBKaNlaHQ3tUqlAP9A589tYd8yv4nrtnbLgMXaumgn9HpS%2ByN6HEXdozh8qCovLFIGMBVh4hG99%2FyIOIG8tpv6BcVzGWwX8pSzPzUDpQMKon8dw50M2OT4g%2BhXvJgk0DAf9Rt92UuQIOHEsjr9LL6KfMAmn%2FFqzAY2630GpBCQG1c6lF8dX8CW4E1MpT7mO1C1K4ikl1EmqpIUajGZz3ca55Zv4L7EgOrAipOgx2PvcaqYmuf4yl2idkRAsQC6Nk6dSUdQ7jgGSZH2%2Bh6HJHrULnkmfv%2FtNhrkkLQqMA1YVzw2mEiXtpLyhcb8jiiR7bpsCm5sDrEikdqvSgGBVLPoXnERslX4QwjiiWIJkIjsr%2BPIYwbQd4oqXILy%2FxCFFhPdPQzDPvmuj16A1exMIj63NAGOqUBnrY%2FJr0mbe8dtVU9sQrH4JaN8%2FhkNw4hSj5E2qpJ%2FEyflowAYPtEsAtcxoxPZ6%2FVMNAm4ipBa5XZaVb9WDRRQGj%2FszEMiaU%2FlOnRcxbA0Dr8Z5vehi32AQTBGFdOgZKG1DpKxZ25WlVblEQWtxdGhZTWGaQYin7d84sBcqXDItLtNzufVrwbszfgvd5kIEHVUrpPG03wIr4Wrt4KSM02iFjfSRTF&X-Amz-Signature=e31c1ee2d78fb4d67d7c758429a0ea6f51147a2a6ad48a95c5cd9745a4b4c9fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
