---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRF5H4YX%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T190947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIHUqoaHEHCAl2KunSxZh1SJezPOHMfp6G%2FlywsGO%2FWpeAiEA2pFwI9Qobx3zfsBqVX33RMoLBBXNwJw1R4lmB%2Bvkf%2F8q%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDIMgpf2OhKNYB98fICrcA8J9KBWTSlF2SmxYDh7dUep8T%2BrLTy8WLwJIWav6mqtroJjicPqDJ8sHQX2kgebYTdT1ghbNa5czE0he2fAap1bA9Zk5pzalP5tfsffj7Xy2ltiZKNJxTTxvYn%2B6UR%2Bg3SGVdo8fmy35198AOeGF95O0%2BpMxB2R4MAPJLyy%2F8kiPyd5ANTDJLSsokvOhZXJ1g%2B3SpuBdCEsqZHfDpqjo2WQQE%2BMl2CyHryvrI5cEj95MXg%2BjsJESO0M8epD6xBacfXexdU2%2Fmxozik%2FbDPTyrzleDbebz6ktS7vsCSnWu8bNDsNkHKFO0SxiKdutPYFCZOEGbFi%2FrGFmq68pNK66rXfXB4bikwGMQzCKPKBc93uRCLWp3STctsB%2BNK06Uc1C0X9JVQkbJB8I7U7iW9pqTjmsbeGMwzO7Nv2rVI13ZKk6MF4eqC412nvwP%2BP7ph4XZI7BzgShkh4gqts0MhlBfhqWSMI97SYiOk5MGfRhW45K6K1VNosQYqqj4l6PZU3u9GieG10XoRfTNJO1R4EcOzbuMqvyogMSwW%2BlUtWvQuZjQ5LdnxymCJFDUQFtgJCfgDdRnqBwcf1JJVYNoZDfYx%2BgID4VS0zzqvEnLjdDPimXHbvQ5L8f9b757h4wMJXajtMGOqUBRaxDUHJQZV0pfFa7bsIqSvLsgRt9JAGH32NYx9wgbb6r2I1JmNKzE39fY5%2B%2FAnV%2B5101AmSz9%2FAoCH%2F%2FqwOrq7BNT49s%2B1PvqI9j1XA%2BQyM37XUKHI%2Fp%2BNtOHBvi6%2BkopQ7IN78oFr2TbzlyM%2BYgKLR2CG55%2B8tHKC88EYnFvR25DhDL87iaSPX3359%2BJJKUEHbOYTA7Nkbj0JmRKnSU8zIMqrPy&X-Amz-Signature=730cb3243e79362c56f660ed48ceb2d2bccc79088c7e7d7ca151738e21a90d8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
