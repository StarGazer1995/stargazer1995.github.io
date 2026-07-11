---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5DRJDYX%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T144437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIE3LzFfXlqvY%2FEnOmcQrgS9DEEWCawbzVkmLPbgxHmraAiEAiXuIpxhDNcUo9eZtNWx7%2BdpcnLMHwuXYrgjPtq9YaScqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLgUB9At1yevSXcTyrcA2rNhWTvqPSB%2B%2FSHO98DpZUtw3dFFXushZN3wZvM%2FTYN43r0bCqprIokSOTvnDkHAoZhlLgF7DhwCX%2F3HtrMiMvUC8FhUr8VSn47jAO8Mkcfrf%2BJoH7hzbe5zUt0Kt3X4y%2Bz2BLz%2BEwnx3xG1naEmDB17ie2ebvnh4SVtN3UiE4U1jZNEERNLGO9%2Fcgjq1lYWi5%2FqaRkInVOrCIj%2FVPmTCiKpSJ%2BLwgGC%2BbqRvFC2Z12wBjSPyrXWGVVUbybaChUuFREH0Ur%2BHgr2mWTCbZPhMIekwB7YhhMJPrZvkylKUElW81gahypII0GJAYe7J8Rogo4p%2Bb2YXax%2Fs8je6RrcPT1%2BCx7B1JM280tOXkPKpPNVGlISGZT0JQT1elM1GsHPCTpkkn7aNvJfkL9yvK2lkBLzZnXCMxjCr2Xe50kfWFeBWyoGq8D8eXmrMNYry5GNuvXWbt%2B4G0VwlMQMRcPLNE%2Bc2bHfhmUBNZV0h%2FPVbb5ZFx3Ncuj6U0i99dHaL1hFxQ7aR673YGdmhdNQray3Nl0hw4qXBm%2FdSAE%2BwJgl8Nlx%2FaJAyQA8n8wxEnlB1XcmE8nlDrab5l3FtNNg1Cm8SZU8TaLsmg6o2DugsOXhIPE%2F54fsiqgK85sxcQnMK6jyNIGOqUBc28A04vVjtgekHtvC%2B6F1YckosNubRLuTdjhnNVAoYZEZidzKctHzqt1yIkvnAEY5GKUuWU%2F5jx7Ijm5yz7Y5NnqT%2FzUFTyu64KVEFZjSSEUNgoIw7lMHImb3wXMkUUzE9GJEvYY%2FUt0B%2B3%2FqzZBiiyXG386XO0ecnkQLpsSPVIEC%2FUc7oKl%2BRoe6Kv6Z3L4gspF05S85YDyfKWg4ICJACTa5L3J&X-Amz-Signature=a79d94ed61d7e0f0bfa0d0f625d2c058208f9a480fc06439ecc6d180b509e7f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
