---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBSBATRA%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T214625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJIMEYCIQCLxbVIlHktb%2BrHnlvcn6sCA8CPp9TvqgqMq6s4PJGOqAIhAK4uoJSzEiRRGo8qL24bUv6r2thrAtXNmqFZU9X1WUqhKv8DCBUQABoMNjM3NDIzMTgzODA1Igw8gvgiZlm4bVJMwFsq3AN1sq%2FmRjzRl%2B9aYoifNX8NrL%2BR8%2BykZJfkDdWUUlAX5smPTJYAPz9ghzhEvD266UgtiAWzaiYM4b8pkKAWSTzxCYOtLYcoj85eKnYvjIgWC8ZeuGsC7ZYDbqqzNA4qzPJuERXfpqors5UDWjK4Scjf6Md1ZqYTxWd2ln0CvlTzwQ36fNozFTL3mkV61JT6fUWQXMx7t2PsHBB97iycF67XHrrtJSC1akJorgSnmom%2B68A1oKt9RFdBlEB6p3NRDY1M36rvRbzvac8R2HnUUxSKcXkdJyPFyfWNwysBdf73V5Jbjck%2FtpU%2BN2pE%2B8mHInImNil1jSSqv0aXhSqiy7VEa9gnilEbS6YIz9hV3Wuj7AaiA4YlPbBRU4kYJl%2BV9sgkIZiC%2FHn%2BBC%2FTHCcUe4utx1v3exsVXmYJdSZ2UzWNWCLBAp1N2WagZfHidiGtqnCEou88d7zkOV0NObg6qrTHBwd%2BQrL7dwcp5LvoU0zvG3izGZTwHrQHgCt3Vy%2FmDnrLpnCAfjXG6DxFE2HGaUBEzzlSHjJ6ITEMkfQ8ih1o6Xi%2B1E%2F0FrBjF%2F4gF4Ace%2FPQ%2BKLqxR2r48B1y14vOtkBRYDJMwthT6qXxmVsBy73hAyTojSuTtGLCGR6%2BDC%2B6vHUBjqkAQgisnyJifillndx55l44PQJvHF0lgwfOky0bM6G%2F4ZfajNyf5SYLVIqY6Crv9q7ELSGH4Ecg%2Bq3AJpTfrGwXKMxyKiggcLi937hKcZTHzhgur%2F92xVkAEOmX3VypDHHonUa0k1TKytgC1GEB9bfPnt7aDs%2BLQYdYvzVtTZcGeO%2Bj%2FtIv4779DtJjDQRy55UXS1CYUxQQPVDrc7WcNEFReP6494R&X-Amz-Signature=2dd86985781b585ac042786edf90e5751513322bed2026e4d3e2f9a5bfa74269&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
