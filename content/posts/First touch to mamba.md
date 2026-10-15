---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMAY2B5L%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T224533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDpouCFQHMpWKh0gbWwdSlEXjtb6BA3zd7TzLtVz00hNAIgSRkkkE1OztIbR%2BcYBkDl8BNgr7fZ0mfaKlFeyHg0lngqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMt9MEhxnpGBjwqjircA7afXfIAdxvpHW9SstYfH7bpO5rEMq%2F22bxJnOCSSSmR%2BMUEi28zn2tK6EmjxP0x%2FgUOdgbqelvTUnqO1zOefc5bpn4Xls2GTDsk0MQERioNexBBypAeaL2MNfAOmQBuFsPnttPn%2BFW5x%2B0nUp7a%2FXQw4uqBw0GY8kgVLCkz61tt5Lp3gjfgtjnAyeptUfmWCG9t2Cki%2BGRWG0IMGJ1cXA8EEcFwoyq4XIZXkzDWm%2Bc0JDHD9CiW2lUUvnfY1o%2F17tic8EE4gkyIzso0natxlSA3eB5YyZmRoIYdJ2CaIl8pWtpsvx3jWms5ousrrBOfOkgaunlQLcyNRRkYB6LSAuXTFUezuC3cGC%2FKwMcQTpTX8pDriGZth%2F2m6Ob6lKCul8SdHkJRP1gT%2BAEFuELNC9iywaTqBGpu4rjXlbs1RCflSgKI%2FrQg1hKurbHiv4SRXnrkpbQ99JJn%2F2aSOWh71sIOBIb%2FzHLciZhIo6n%2BOX%2FOg%2BR8SKmxYUPLbZiM1fkO899YsuAGpOIsBcjStrWEvVAvDuJLDBl79fhfBVDV%2FWlScgpPRRUlQz4ii%2FYelfG7vt1vlyN9sYO5hAqXL32LEAtNVDlgSILIc%2B0ehVMi%2FDpBZvk%2FPLUTqwNTvdKeMIORxdYGOqUBORkix8JyUza0yva6ZVVvFhytLIklZT5hHBLzIZew2XI7bNWJYcnOeCk9v59GYZdKUeK03k5ZEjJMHwdZGDH4pQ2Ahm2cVITxS5NIJWW440akmZjk0nFMDUl4iH8cYhPf0%2FJRpR6nBUp2qXId%2FYGqynLgBbR6WN5REq9E%2FOuHuoU9iVnJxOzQpupc6rZ7wtRV8nz0gXTz5MU6MfditzxC%2Bo3UdHLp&X-Amz-Signature=ec52bc1a0152d0ee13308a0062db73fe873d2a6fab577c4a1efc5b514584358d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
