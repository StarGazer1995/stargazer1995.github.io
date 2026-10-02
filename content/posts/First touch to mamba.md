---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DHJC3U5%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T141557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiX78jmiS4uwMLsLrLx5sizpBcA64yII%2BEiph4UqxqzAiByYJXVCtprV91ae%2BTq8tEPXLjKuGyokbmOeFANS6bAfiqIBAiX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUbb%2B9Q2nCvMDea3cKtwD1YHDKzbEtaCuuf2rhvBC2QmQaq5PV0oCmNq0gV3r1qC7UNlZGqP9r5r3zLhHshNhGHPF%2BZ9VpRaEKMPp%2BeLZvuR1mvVrqRdk9JecxEv0Q17vaR0YMlrub%2Fn76ARdjrpY3RzA%2BQOLQWgE7H9xHNqki%2FtAzkMUE%2FLdSl%2BK3jNYCR7LPw2jiqe8DltfQv%2Fd1nOTjb3VbiyuY7JxzbkUvw9IpyInzQsiUMi6L2URrdXTb1G7vYvXrxQSN%2FZU%2FfWyEqfX%2BTip3WqiOc29KXqs17waXDqO4SYQsfuGAotQML%2BnEX3mWq4nm7kHfZGm4hsjqBVmG%2BuU5i1TSuTXQrDQXUvMjseWLjA9UxpLIvVGiWNDCNeS4jiwHdR6djpM2vF8es%2FtaHY0jMlounaB9ThTLvfLZ3w3wpyMm2l660SXWOoSI1rXn1aun246HUyueIMHx2d7Iwg%2FHsRAp6JnluMGknYZZ3iHqgX9y7e5eVbXYBRioJNdW0I6K6Eo%2FfcUs8fAcNFzPG5KRTzEE71Hi4C5Gn6NJeXqansxmLyq%2B1mAt2F5PMFA2aHYw6T%2B73FHubISmLAH8PC%2BqjEWVVBXzj7vl9fT%2BGIYCEGMEuxyMYvgPzHOsUpCmR%2FpswKNU2hsRBww6fL%2B1QY6pgE6emXHMjB5Lxnd5rterrXc0dssOfyhrZJG4rKMO0Trymn0ZCAQW6lObFveySaOXZ1mqxYXzD%2FkFM2VDPViMnvdbAfZdwY3bZJLcSNfsgsZm4VBldsOVw2aXkP8yGdnwtAsjt5%2B%2FAVWCgyO7VCNmVOfKGAxFOkzsO%2FjFZN2llyLWCWfn6BfqFcCiZ2QSwY32gX8j%2B6qAfJHD7m9qniLPuz45OCoKI9h&X-Amz-Signature=522b083b080eeaaf7dc63aa97c881aee05db0a52d35eab00dac3bd93107cb6a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
