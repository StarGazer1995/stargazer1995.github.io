---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCV5EMO5%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T221515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHLbxAITtcKQbs89mRtljqx79Oz6I%2BY%2BxjkOiaeeDryUAiEA3n%2FZZiiliDpbV0tdIybUDRySndF%2Fx4cgNG1FJWbzaf8qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBDem2NAwaJi1AvSsyrcAwX7duoZBlyVEZmBy6M355kfYATojBjAiTHpzM0rdziBZ8SSzmJaPHnjpJ2m2GZ6R%2B4TYJE8jJz9nx8Kt62onZqNcOGEAceI4xlAzv2UmHM2FsooEuWL3tXeiIr97h24kZluJ3WVn%2F%2FI%2FpdY%2B1s2kthiVL%2B%2FRoFLg9aauE1N8sDubHp0WNOVKP1tuUXl%2B%2F%2BxO9%2BW13kBC0tfq4LXqGzzwjDYj2VasW1VdCAzpisgdU%2FiOpbSKUECAxfi8SnC9qNdPtiVw3iXCzCE%2BFyEHuuLiic9uq9ysOgpEdyBs2uaYDoUXUYWw0VrYCC6IVPSq1JkEgp6f4Xojw3fUTbt2VBfkFsHP%2FVpDbdqJimwWkctd0CbNSbGm%2FKuSs513r%2BadH2DeckwcApiUqxVSXu1PjpvkJZO%2FGP2lIvT2NsX7ebBVm0I9ctLA1SDwoJicvZt89EVNOv%2F0hrXZYfUPEbjeqkYbCIbQV0QECqtgDetglURU2sGTexf%2FW95quagm8qlB73iQ581M1ye6bKMkPZY9KTf3uIUP6dp2NKyM%2BBSZ3%2BxZHdvoL7iNVYUrCjzEfgEo9GP39nTnkUi4l0%2Br%2BShJblSJN%2BFOL%2BNfBAd%2Bk0SIvg6CpHFUxdStDKP4JXHv5p%2FMMvyndQGOqUB4YIKMDWqGzO28JRQGNDGFuh37mpq5HXHO4LjTIoMdHUx9Gfx0vjwXa3yUipMwLw4CYiaB%2FGtRjVUCtTeLdfKN5DFmcCwqMfub1hSvJSoxPty5J4EnKmMBDeOAMKbd9qof%2FIiU5uCFUGwmtsrlkY54Tebb9eRsTuZI8vCw8dsBT6CmyAVgoYpgxqqvWr3H6sNfTSgpAKWYGZFWPsDJED77YwA5H8O&X-Amz-Signature=13a2d7c5df612cd88ec52d8302c35134247c6ec0cfb778088d3aa6e0ae1fee21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
