---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNIYSYPD%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T085900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIQDGxl%2B6Ng%2FqUFctNLe5%2FpbFTo2MVA1rPzMbb5jQFE0tWAIgJEKuMJy4EcFniCMFDcQpShbHouDP%2BHepv4SVvNTXr4EqiAQIyf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBv2ylrpsnyYbeHncCrcA%2FJe4aJrD%2BkwctqyM%2BYnHqbgeOuCnjbdpY%2Be7FqJFiSkODyJD3B%2F%2BlhPniyJwmMsNgd1I4XyPoP4C6%2BSLBMRRMi12dBvCZxtv%2Bw0msCBYTMP0Ex5t4yOV6LKg0PSQGjtpyqhWwkwyd%2FIRWsEDe9sjXlm8Oi%2Fdmk72VqjivVdIKf%2BRZuHzDHoMkbOXUs5xpIg4OlhE2sN4wuTMiNNNpKrEaLxc17FyQXykEr%2Fv1UCVCiK8sT3KBpj8m3btHPCbpPlC4N7SvAXvTqRBfk3GI4u%2BX1apuDbXLBcbCjVuD2TP%2FfLIIJXsiDHGa1DVDRBJuvm6KlF3cOhgkjbPB1bkDVANdwf4hpnBAIEfGf%2Bzr9Njemn7bkjFbDphneNT5jTL9Brjbt%2B4MPpFqC8WfQLkK3TwejCVCJyrTPdTAKN5qWtf9d9Y3gPuWKevx4oNXBMGUhSyAgMeID8S1fsZwU9TGPP9zqrZ0GLvgHgY6KUDbiZSExWfJ6MEP8XJItyvNT7X5Fz8QT%2FX8gDHZqFDFOz%2BATsuSoXE%2FgQwSa0L6x0e8HZ%2FqXtq5%2F4igOvAaTFn3%2Fkb0CZ%2FyTP%2BmjsOZZ4OBLBEsFYMJoWPrv%2BhithByxYS9PA5oPnSc8dkrCsPEk9CkF2MJHZ8NMGOqUBh3uQTRY%2BUNCVNRVI6IDcDOL1vBo38k57C7P6PAFWHoHSlLOqX43im9%2Fa254TsUHRQa6Ub9Dg99UW5sttlhAd85W6d%2FenhRM17XkCMWAdky1FSLmQV2kZTEVzEj3K4hUvz42SEXrBOt1G%2BU6uIFRJqhii5O%2B5YyY4HloGSD4ZlI0rC2ZiuCL9hzEP3dNne%2FQttsTcpg%2BKNBOGmfsG03FrYkXKd1D5&X-Amz-Signature=55cb22a56f08a18729f985345bca8184afa02a6dc0abf21f36ee515809bde923&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
