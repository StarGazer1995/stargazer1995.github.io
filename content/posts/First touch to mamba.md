---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663N77N5KG%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T035502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIQDc4gS0j0JDFUQ49U4T7zDiS5qLTCVPjcRvsTh%2Fyj4W3QIgbSEHW%2BmiPudBwCY3brTSvowyyz5Nv%2BwVizGnK3FOuiIqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnXZmCAG5MI6KgMlCrcA9huGXvo4yo5CgFuSPUJguS2CidtmNQAAl8wZyCsToZ5ytP16DHCdNNRh4kTvMTUuAtWFRShtAUQKwymqzD872j8G8k5Y5mMyieGBISrrA0lwp%2FQJqqjDMBa%2BwtGZU1oL0RpAUEnhCDkcjEE8tzPAMQ5UCo1bNjej4dWRbZBcIc%2FEcwoJT4bySqjA2bf9NHqTyN49kJ8sECYFisW6c7Y%2BnUNwUe5kUSmUh4G59wOPMnLKx5TLs3NOPwAmwnTcRDG%2BFpIl4pvL1%2FCQh%2F47LG8eqxPWNKGY6o6pX5ow4L%2FlmENLmnHaDXpRETBOCoQEI7fUwiLhgl0nc6YGA559hs82yl7bjCEXzwqF%2BbK8bBSmEpdpGeoxulvCr%2F4JI89OFOR8I4GUK4aaFgRPRefCiWAMNrBP4raa2xb2KRL5MY%2F%2FdmShZARk7Rb9FztJiGvtyrIuD4gQISXPFgCTz1eyIyNDvSP35nEIAkGnT1npnWfrJBYxgaB%2BdtwGLvwEfnw2Qkxo9GIv9KLWh4rWIQuxmKX9RhEDyPzDj5%2Fytrj%2B74O5UWx4BSAjdAGlrusTfrqjL919rXzYVKl8MRHFNnU45VB47z7K%2FcRCMysNH%2F4k%2F6Ac%2BpzxdcQhVwgEl%2FmR%2B7sMPGf%2BtMGOqUB802m5%2Fi3bLczNUB7wC61K8wWXf45cgXuIZljmVOYLI8MtfNHDU7kUX7ScPAT2nFI55tiR96er1uoSgNe3u7k7yq245mR0z7IvyYmI3YJR%2FWSw73McdBf0i0ApAgdcg23g5DPOEecNAZbSKOjKnKkbC4MYfE04li%2Fyk6r4VtUCGVYG9MVaEPlFzXev1eciU8%2F8sAJOufGzMkeEytl7%2B27Fauqn2Gc&X-Amz-Signature=b7b16e1f60e5cbbc8841df580b3340ddc253e33bce1f9c12716d670255dbe7d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
