---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMOYXNNY%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T191406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCGwd6OO8P6ZqL7d2TqoVEW0jGSkaTjKDwVLCTo1yd5eAIgAeoa5OHoEIwpWXluTkZGky2SqWemyXUKe0sjbzkGAa4qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDGvJpy5JGRJBNL9%2FyrcA5oFdNLlR7lIFUsyoPr%2F27ExaYN6giWYB0nbm6G4nLr%2FvJJ7YZiBX3EnlaEELw8HpPJytKDwOYonqu7QmvZxKrB257njBt74YPyo1L%2FOkdeIql74o%2BG51a%2Fv7a0ti7aRXyvOWP5ImAWavWSfNWadpO%2FYTEDblHWtH%2F5YEXz33puUoFvwJAEoz0pSL7wdNYOMo39EvmCv93yTHQc6kD%2BuI0%2FAJ9Btyd1SavbTORUp5LRy4Ua1n1wnwk8Ko92RgrKDibOYvv8YN%2FoQf4pQRKrkjh1jeQy9blNf5l0o2uCaIz%2Fd1AOxUfo5Y35f5QKDy8U61tNvc7DJCh1VPMaVIaxFicji2rEjZipMkHtttDcQELh31UhLgK7PNFo34kvEFWE4yLUT415RJqNnTsgG1Deq97itRaPwjt8YIh9E7crskkciaiTIcA1%2BigKiwnQ1KhguWnOTmO1prWcixWOV%2Fh5Sr1tsi%2BHti74CrApzzG9FrY3w%2BOCj0rJShU0u84ziQvU%2FMdi7Dq4kYNBABZ1X5GG8vgzAg4%2BJcWHLDrypIRBB33TZC1AeihgS7bTKcJSK%2BvOXZU5ApEXsKnC2FH1wRXxuOMf0Kl71SATuccfrCkq5aPRCUJeYxVdgrYDeYxNzMKzxxNIGOqUBjPzw0VXUZS6IBV5RDf4Ta3%2Bm48CdaQxje5A1ijo03W3X%2B5%2BzbnR%2B0WjLpuv4G6FMbD3FeiWKXiGvpnYX4A%2BLKn7w461FGnm5VbPtnsjnBo85eNansW4taRvCrNdtY%2BqaJoDzdnBnzGUeqknWoyc2NXHdBuo7M%2FdthMRArmI%2F%2B06yoNl0x%2BkcN4k5iM%2BMEH8nc3RFJpNDjEe9Mu%2FJhDxvJ6t2TNM3&X-Amz-Signature=be890c30a291a9e27558fa3cb04de2b58fa52d71c8bdc4e1d39a86f96b23d7cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
