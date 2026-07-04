---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I7LWURB%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T111659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQD%2BIUzIQsljNoqYlelwszlXY7HWX%2Bv4VDiAYSw%2Fmljo5AIhAMn%2F3Qhntb%2F5tYGGfH7slcEQ0R8uvH9TjOfZfheYueI%2FKv8DCCMQABoMNjM3NDIzMTgzODA1Igy1B4SDtRoqLVdifN8q3APruRQQjlxatChI8qsVpAaRAYKoenAFO%2FcHBAjH3OVz9GzvWg5sSb4yzNb9B1sK0YAvvA%2BXnuWh3rHveGXxk4szYIu9Vd1BgdWGNimE1AWQGSnOBBgJ9bPmJng%2BYVodv2nOzg7Rjehm8LyCD4fzSK9ek8vuAqr7tSxEBG%2FBGoFNnEFdysenMhTnjnYERbMIYhakLoAHucI39DE%2B3ju56uBnh%2FPb9wnXEdDhjaXs9qPfcwuYjcJ2O%2BisJr5fmAcfHoLXFIAMw%2Brv8ERQbGMXJosxu6%2BRz0AtJxfjIrd1BXDsW%2FsiiuungVszKNzFAZaWz759xXafLlK4TRuCmZLGaHK8v1JX0F%2F%2Fi2GGfIFAZXnnE%2F7eNkFYthuwJIkYzbsGIDz1WH1uQQ7wCiOpya0KRzpzhXxND0fgsi8gi%2BHoA0FH%2FNVLaFWS5u2ZwsNlh7EyexUH%2B8gxp%2FSGjF5p%2FsdS8U96Rweoki%2BzCivgPBme5bb0HS%2FeIqkjtd%2BF%2Fyz5jutw1gRMLPClI%2BQwiCzE71PV6ohc3cqfSUSsoLHKsc2xIBRzr8Fi0hj3W0f1li1V0yPsF8vuc6FeBREpSttPuZT%2Femv0CT3EgjKc9ChY44fpowkmQTVrrCYQDSkBhihgbTDooqPSBjqkAbAuBNQevu1emlPtj507c%2BYfT%2Ba6ZoGEeK5TZMbQnKfiQREG7XtnXXNLeAZrYtEMua2a80bz7t%2B5gHUrVk5V3YR2lX%2BeGs72w3w6ekN%2Fc%2BCOpIxQHQvkT7YqAqyt8aD46nbfn7etJ3WJfIIeqh2ZIbbRkfRpvgXmx79Vuc8veEQq8bEjRuD%2BNVMcTeinBDXbo68qh3sOZEn7k2QPeWmDC8Uqd7cr&X-Amz-Signature=513c5b75c08f55cf69efd07a0e4961e87464cb83ca40e0d50b7f2443aca3ed95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
