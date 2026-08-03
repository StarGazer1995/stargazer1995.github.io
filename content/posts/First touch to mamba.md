---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NGPW56Y%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T013343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIAg71mO1SiCwuVoiducCnLbHGQK0I9%2FhWMUD5ybUBBOhAiAxSfSHIxSwV1ZAFrZW3%2F3n1CVO0SiuClKC6s9NQf%2FU%2BCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLslYJu67XqQDesJhKtwD3jUHl%2FTCfBIYbFTIEvtXB93QJcuDpEbJ377YRa9icQklq4wgvywUiaTGMM0b0BJxR056REsLwiKCS%2BO9cw0cyGlfxlxfDPjDVByYFMBaaLqsrlImDuVknykbDIYfnKxjbYyCdhBmMiArRPYcG5A6qtcOdA22YpCIOep116RLCOqAoOXC%2BgaXstf%2BmyYkJ3rT2p2z%2FB4fBIo%2BOVo8cZZ4pG8Hv82J9n03NUJyvfCV50YAQoOPTn9X%2BngviwbOmtFn4vhKE42LxW2UNYdss495%2FsUhAg%2FlgNWT%2F5IawYlkro7pBu%2BBYSfqDUnntd9qfjE%2BsEvArtCgNgyb1PWJOE4c22SQ62Ln%2BLMnXXcCguxFiS4AgH8fHbBuKm6KbEmFJqkuON71flfmt8%2BBYOVjOUUixoQVkMeG3MOBLjwlJqYqA157NfqDX0jK2br2C5UekUzoV%2F4ScYZk1ZGp%2FOyZbHk9dO2YrhUYrDVd4g86jCuaPOE7KSXnbFIANnu8Pa1y2L%2FYS2h9ePwE%2Fh2zekw%2Bcdil5BFhyL%2FwKHI9%2B1tGDw032OawAYmuPA47dwtT8nFXiBPpD0ZzP0PtoFAfDuq4BPLT%2F37ftAQzae3CL00oKUn6zM1GkXCiO7fduP9hD40wzYC%2F0wY6pgE4JdDsx5Ox%2BZlSQqX0vbFnlTeGpjxXdfiOklu2dKteFfOJlt6cW1l2KWZC9QKShFBwOPGgK4YGlYvR9PEcokiTiZgsQd3Bo3d6XxN9g%2Bql9kSWpmjmw4yohFiPA8asH3B%2FRaRKJp7rKC77oVuCWueMOkqCspNsmAMzKKbp8d2J3mSmPgGNeLwITc5Sc9EK%2FbDhrrJt0kwdyoUsbKn6LR3E5sTVzoS6&X-Amz-Signature=880b2459840d3c97ace009ef02b0e8b2b7ced6969a952bcf8afe6d67b954ecd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
