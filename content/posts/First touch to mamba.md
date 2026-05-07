---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HMJZZ5S%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T014816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBMMiXm41UzrZY4szdtT5pMSbPSxcKLGa4nT0ErOepnZAiEAp0ht8AheM4t4FYDJHN0GoSl4%2FWgW9tyg8mno4%2FgOAU4qiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuGJgHEh%2F%2B2oHwghCrcA5FZrQloLTaBFdSUhN1BLoqnsi8WkN6zcxMMnvcmqX51vjByd9GxPnXfb1MFHD1%2BHtuDP7sMUfazQSj8%2FxiWUQ6fDe2zotrthVIH4ryJrqxu%2Bf4L1eCrKk%2FHB8MzdDdODeJt29uG0zwu6K3YQkblVcJUADr3rcTF%2BbVesMQqWCeTVXgGx6aj4GjxDeCXIWCa8xfGz4oiG6Ju1C1ONXgqJScXE7sEYb%2FvG7gn2wByIPVX5F1jSGZ6P%2FS%2Fr9kIFPJsP85YrhMTr9ie4aZLgNopgUdBuumvaoWbaaYNDvlQqSWWbDEIa90o0wmRgqVCG%2BVVB2lMbEwcM24EotqI5u3tMRseluf1oOdW%2FFvYlAzrVwcJ6lMH%2B1Egn4UK1PU4%2FFo%2FynmHzomvY177oDgt%2FzY859A2AY%2FkyA4ZdzO%2FrSv3tU%2FSB8dR5gjKGhFbrigpC8IOR7dj7x284HRMvK1xonBcoi5T%2BfmnN2jlgwaAnlVjw1nkHkUiZ27oK%2BaHI0dO8koF5gQzwcdoyQkzC2ebFfRmvzDbwOSFswewX9dJAmapedvv6%2F6QMToN24kolpEj9y0%2BXhwFFSoA2fSZ2M%2FyjSF614NHfy%2B97j4z2XhcvDzKjLdXwV0gKT1J%2BjYNoxfmMPDG7s8GOqUB0A82T0BJvg2FYCdUi2vRhj9vkgGGxGxyBV4sZQPSckfhyXFUnZDezU8MyQAY6b%2FROdQR%2BA%2B04ht51WP6uVlvCAq%2BtMN%2BjUd7ReXHmJP3tTlP24w%2BH9exrTRt%2Flct%2BSSwoQ1WlL9lr9ehVzgD7vH9CLJj3zQrDUBYTm%2FHYGk8gplNWgO5D915xjvQfmv7%2BXRE05nu5vVgADu4yFIZ6oNgj0UXd8%2FU&X-Amz-Signature=69612a97286c5ab2c3e519961f6253840bfdb11f5429216ccbc6a54e6de0b84e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
