---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666573UDTU%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T132653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHkTgqvtyUxKdRWFZxuqYkxdJSdIuSE%2FGxUGa%2FCJWyIVAiEApiC94rTbqkIABWlxAqtz66aDbCLjszB%2FlJ%2FMfex08o8q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGfhEmFKj%2Fl67XqVgircA97iFEC%2FkIZQkFwOomWbZcFuD3IaDyoMpB8fibZSqvfTza%2BGlarajLmFDYmdjWqy4ZP4Zm3F6zNfXuJMcjdjAUrTR8bkEWTJFWk2%2BTquN2WL6uaWRToYtBIVmLgNHEJwJF0%2BBoukl3nWlpJEtYyAumWUcPHFturqboaZZ941URoJvEdALYKrx5PUGtUTFAWGUFIEf5H3R75vE7hjPTFHnRmsL70A4syJDJt%2FxierdzUAOo3bauypJTAHTGuFQflOkwOrO5GI%2Bm%2FjmbIHnDIye5zXKjka7edLfrXKb7TBijZrG1x%2FmXbvgbx4nFoO1D6FvVl0htv8cEY7xg55HTGI1UkRX1HoNDGgplvX3Fi5cNcl%2Box%2Fs97L%2FYKQWDMPmAp6wCgaMEz19ZKAkRnDT26s746uAdcONsofd%2Fi1tLfW%2BTMCRuk5t8F2VG54MCGrHHSx6GVNscormAaqk90otQMiA47RTvj8MVlTWrztp11ihxCOHLBuGy%2F7pi22ni%2FtGfx9hCVGiXfpQkc%2FLc3nQxqX8wk7qzvW0Fd0WBqpKieU4iWb%2F0p%2FOIkEVwnZ6KppZS0o2ftFIdsezAnbEbFMYBburPS6FT9G0V0EUS3zyUxcwiaEsO%2BkAjm%2BCVMWFKIIMMjRotMGOqUBk5eALk4JMiTRS%2BMEwjMYMXErXLGCFxQbNgLjBYwTrPbqZIspJPqdXKcytpwCSC1IltDUAPrnDbUhjiyD1AGyjsRyDbocpI9nB6qoxa8MLY0Si9S3lN6cZZT%2Bl7Zb76bDqfbPpPIRsMjIihhFg31qofG4JTbvspzskr69%2BT6YopudKOgBb8xa73TagsnwUXrg9Q0L9tqwfVVx7rUPeD4FRqu%2FY5Xh&X-Amz-Signature=62cb1ba9ceaed8b61781a899f9e665ad9eb345d4fa68dae8e0c289a2086eb73a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
