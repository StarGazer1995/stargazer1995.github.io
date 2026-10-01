---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2MXGFHE%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T005451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHzhxFFc3m3PwNix0lJCZc9TNmQk%2BW2WuHL%2B7CHePApAAiEA52AsrJWkVnwiDUkxFOSPxTkgp2g2E8892%2BMU7%2B7MV6Uq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDBxpWgI%2BpMQ%2FN7iWxircA5HZ0cTnSfrWAyuvqbIur2VCQ8ZkXXC%2FDl0b13tqlcZgUC%2F%2BveNfU8ti9L8JCmYOc1F5ldtfaHL7cqweji%2B1S9oRTxQckt1o6s2lUGVMTLv0Zmbh4vvzYTGzHR1C4d20aSv5kC4fTKyKfpDb2gRFuU7xSW2TEfByI8KRMBlHy5uZGlAF0XY4IR%2Bv0I53SEi0045gqgF%2BEoyWMtfoZBjjH%2BAgxOIMgz402SHRpn7spu2krv8pi5L%2B317aycXmkP4rgelNKKznEwnDZMX1uJQb%2B4HpBoclYveweLAFu7lXXPSHZRXjvNMkuK5ZWQHIOuEW93oIBgE2SZwcxOVOQ97wurIC2sekdrFjplQmkVGTvBAAukc%2FRPUQBGr0zm1o8ANXhRLs2rz7kjxQ%2Fd420ZTkL4q8eUs9i4Desc%2FyBpITtEdBLWAB4RJJeRP99We6uhfGNdiFsLx%2BF2A6vZVUxo8ot26%2FyZc4EtpW0kR3rq3JtZeo0tvEiMVR0waUZY9GbXsAYBI6dk9gRoPt526EwTkn0pyqWFhDd4D9HIuEUwVyIMVBv40BUa6QnBcsAACYgKLVfS%2FX8sUCiMR67jA5eibVmSiw4LM70pSACKY%2FDCxl2ghsf61DOFXucRCfdp6%2BMJWi9tUGOqUBHpyAi%2BXhkg3KcMKXEUZd3j5mSNPYPk6JFa97oxmqCIvuseoyJW3Yu4Nk%2FDqUoAx%2Fb5OTXDQfCzymd4x33cjoUE9MZCiVNKe061cUNgGWmeqY38gsGfFPwMyB8QmuKudbfEBEcL75ZNgsCTCExSJJv5ska3fOV6BRj5BAZL2CSOLOK0%2BL8BtHEP0Kc7JEjQbaZGlh39yOrPxbH8E6H7SdawLxn6Bb&X-Amz-Signature=dddbf3e5e08a563b3a6f3c1c6d734197bde5c101c6bb944b407c42f488dcd96d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
