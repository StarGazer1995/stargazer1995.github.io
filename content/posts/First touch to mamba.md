---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYLUXMRT%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T165132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJIMEYCIQD8eXmZKFnMw8Wo%2FMRkd%2F4Rvic4NYdo%2FMoi%2B9C6eG3nLwIhANFJ03n3V7MAH7ZPfvlHLC54na2%2B7IHGwlFPYVl4bfo0Kv8DCCgQABoMNjM3NDIzMTgzODA1Igz3wIda3PH9bmnk7V4q3AOBwAZ8AQVs%2BGdN2g%2B52xdxEQ8fVZ82zru%2BWdp5MW9IqY%2B6AUKuWMwKz%2FQWFHJRXlCzWqZYN%2B%2Fxw0wjiooDatWTWPr77Ot1SlXmluN0mwXRILbncQtwg2ugJ4Pjsqx0v2saS%2BvtIBmxfD%2FMTNNYCl9P9Wdnyk6zA3u%2BRfwE26a%2BXhdcAb7DlUJxQc7IR8OMMqqqYOfJ5soczSgyLI0qCwZmTbqA8Ihc6RgAurvlOrl9JUNectzja7FXz7JuGCt0OLU5LZXSmUDclpE8MDW7o4pW4AYnlX%2FOe3GkJ5tdyY6lKAYjBms%2B1Eb0KAD66TF547qMgsDdf2i2wo1MAuhiLmUIEOFjHALd20MZHzDcpgIs5rEUGeBAJbXezJWwuK8YMrYpa4%2B%2Bw3VZgAJ%2F%2FsR2cn%2BngjJDckYDX%2BNQlfm%2FeAjeSI5B5gAxjqo8h%2BF7PGpYtqFbezUXnl1VU0ZV5C8Ar663Z9XQSzySxC9HxNHtEw4ZlK4S1mvJ9xpd2XVTowNNz2yNdZib%2B1pD7oL%2BSYaRSEDsxSopilUkD5EL0YMGdHt%2BF9tCIw0OqEzuTcWirC%2BLEJ%2Bu8h0pbi3WPma7zdY8DV3SK2F5oCyLtbj1ed1dHLKxOGS1%2BTsCJvu34i9k7zCBxaTSBjqkAZqH17P7cbeOU9qBYZ%2BiDgBEVO3Vo0suGbe628Bt5%2B%2F6qmR72knbZSjCUTjDHOHsk9SlRrwiQvvzzqcBSv1PQh4QclzoEihezz32kbgSdaH%2FjCBrvHkdHzAlV5qfkFg92HRisGx3wZBT4TZG7tWUgOjHBxqCPjPRWG24Ny1eUd0md%2BgwPUL7W5s6EHNPvFBhgngPMOV2633cbgKs%2FCK%2B8Il93QA8&X-Amz-Signature=5ac02065ce61e209586ef36b721791c55d0d24606cf20f94c5380f6139694283&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
