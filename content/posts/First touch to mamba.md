---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZPI4VJE%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T233119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVGlVquB%2BtCtij8J%2F77jKnKnDLRuuwfx1Wbw94zYjK%2BAiEAvlQ5M8nub22GPglpwWT3aXR0yQQ9Bzr9iBqOA%2FlcRuoqiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI%2BpQiRTuE2A9LCE1ircAzCzFHleYGHUoXqzBUeEIluYSTWSff9rmiCgSunz3DWEvtP3ZpbkUFOe0fTwCA%2B8kq85IKsWsW57l%2BCrEGMtp3W5EIBfhLW3xAzjO2Zpy%2BInyI6dI24PuDu4T253Gm1D5FInFQ4YvYR2bauRQ0wzF0nQjXgmieB2YHQylLiphPyYtVQbdJxuZxatgg%2BJsVPNblVjNvf55BsyNthpWLhJ2vngiySl46DAU9uF1TL0LFxe5PFuNMwBNovjbFOO4RgU14hSKr0zzKjCNASk3LB%2BPB1e0cgOZJ333A%2Fp7jTUDmRqBzp35pgr3kyWUGPtMpLoU6xgS0B6pXT4WkRxIaHkNKMFNZj3ITuPR%2B%2Brlfg7NIi4qpmy2SrE9wHW5ff4QRHakJCEAZfR2ErA3LWnsn7GM1%2F%2B%2Fu0k%2BU%2BvUWPY65gq0CL%2FPIKVbYM70bSNCiHidH56D%2BrAno5JGtYUYr1FQ%2BnO2f2eFu4y%2FU2kRhp0gwiEcSjnMW7x3VSbX7gtVeYR5ZDUXuGMIlcOolICbAJlmwLy38swfaxlACUjRCt8pXSbPaQcYtZ8ILgyVmztmexedfpRuFcgRhU3R5QR3YlU7D3SAJc7zNLaUe8XJ9dC8QXr3JFFLVDZd55j4QpiFPrcMMStl9UGOqUBhlOCRJFs%2FIfcvB6uvCcoVWBjGMIbHL%2FCXD8A1yZuo78%2Bw9RM4oXtL0CLpXQLD44YY6Uo89RR68ijvov3CZOKDCTkJfm3h8ix4Co70qps685oeOLRtCbxMUS%2FFEkxulqLPR%2F1HomOmvtx01hdubAt29AqBxKkQNlus9C4eQivFZHkamLRiTks29cFmMDAdWYbYruv05IpjO%2BoL8Sr7NgVzQF1IM5C&X-Amz-Signature=a8d5949f21e4f472c1522d0b44e8c83df170ef93c531faec9dfcfbdd725ac587&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
