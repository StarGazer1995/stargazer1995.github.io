---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZFVXWFO%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T145422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIDciGUEfH2JJOzj271WTL8aUd3vxPm6odMiYEB%2Bcd7JkAiEAvcSPSaGyYggMHB0TD1vgkXzhwTrndqQhOM%2BDdHZkfkcqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKG5b1IFR9XPKQsZ7SrcA0H00UMWCH7uv9vIubRdnxs1zHEslVTP3Vk3nJM98iQZfULz3KfmXSKGpBwn3yiu8ZSkTgh7kEl3j8IWZQkMB6W8cnWLKqUGKcOg7cjWQSNg6gjrR93R%2FWWqnpbSfIhKxCSPy4q4lcFU8tmjIfzreLCoBKBZwlF8hXdpukovMNy6HHdJvx9N%2FFkICrs0iWeJln1t%2FR%2Fp%2F5uDDoBjv6NMENo1B1jzdUerQv%2Fgu%2FFNU4wZdTKqHE3zB6%2BXvbv1KZSC%2BTMXCpey8H%2FLVZnTeBpCDYVSnl3JSyLk4frIgw2PH8cB%2FBi1Zmo%2BIlt5BIBsRDy4xGBs7TV05Fhekl%2B%2FKHDw2cucAyri8eoWGKBXuDTNgmiOMfve%2BEBsLPiKMcP7xryUOA0DThTpV6A3iDXN%2BvJOBWe7mGheYfds6GiF7sYS8R%2BWwgfKq99lCow8lmmsiSDIyx8so8y%2BpWcn33IIND6w%2FsixNh4ISQDiBjug7SXPMNQnXLUIm3gfKZUj0dW6npV%2FMfc1%2BA0l17DPWr1IV8rfjQmzswUIL6uEo3xPfmDVVpdjOmYh%2Bd49vaSipPVoaXw51IcvLZoScFILY6IP%2FZ7TGnkhHXJcerg4n6RzkpoA65CEluNkCmdXPWkSTqcoMLeSvdMGOqUBT6a1MKErC%2Bkp8BHlrE9xcUY98AqR9gAB%2FF2haRuge3I1UOQZAaYN1M%2BgaCy26ZMao5YfHlZLlIWoz7j60QKR68QHGcKDmCl0%2FQDVZ8pb5BTqjR8Pse03W3vKI9YDPYOV10YvNekTSZGb3H2OPKshK0EsXp%2BI16pxVahS%2FlrlUwWtp3BDganTzyYl86qmRWLNvd0%2B78MLL4viCz5Ef8iVaYfvokzd&X-Amz-Signature=70d0ba8277399e5e19428c83934ac54c7dc3a786d77807b63710b7ae08525dee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
