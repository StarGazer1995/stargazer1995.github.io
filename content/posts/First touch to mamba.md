---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGIMN5WY%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T012230Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRr2tJde1E9hQG6%2F0%2BlFMFYn5uzM2Dz7Db0Zf%2FRANVNAIgEVjabNNhgca9hoq9pFBXabExC1tZlwGfh6xGW9E%2Befgq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDN1SfJY10EfuTGxRPSrcA%2FwqqILygPjPQHQ%2Bwrq2L%2BnEIRHo3Lum4FN9YfGjICSnShfDV1scNHR2niR%2B3u6vdcBsvgxF361Azi0%2F4nEb%2Bmn%2Fj1EBASL8bQsF%2BtVqMP11rCZNmvGLMkviTi1ltLi2FyoU0cl5ny13ZBNqbACg6SemC0Ow2%2BPSb6%2BmFZpUYZcQZ3VI%2BBqW%2BUcwCYIGffhiNG6kWmfeh71ixfrPm0CK%2BPAM5X9rUV2CDJtbC484mUMeeRj%2BIhhI7n4c48lmNZw1URbS8u5wX06qTNdxT85JLvlAlUcdMiqSZ28Wf2bi4%2F%2BkuC1xAH7ZVbktgF9AJ9zRpV3V3Gq2ehPg2cQG9YugzQVnK1%2FsWGVZogM3NqV%2BAbrwT4vi7c%2BOqOMWIKi7SxdrzkRTkbEoY4d2ckS%2F7OuH0Zs6vyUdVXcA7Y1KNmq%2F0uBIh4mIJ9WLpx2eYR2egmCKfGoYOONHl1T9gwcB9kRqZDQED%2F9jeTGAI5Mek2p0Qa5iLwGeqmblJdZrA0gDkQg8qB0sUWqw0ISjsC%2BeNGNy%2BEpLmNeoPxk%2FgAAUdSY5VsAuKfCqbitUxsq0UH5qBSBpYYJUr6alEBeBk0ztCeIJRehsP6v%2FTNn46EroESIBwRC2NsVBGEDapYoTfyDiMPyhpdMGOqUBVy%2F%2BhyyMewqNxlATeXFGHmANlYr91uLD17uOUf5leSF%2FG2DzP6AD47XU3vHwMLhKl5u0%2BuXa0mWRyW%2Bv8Yz1o9VY%2BpaEQ1CtqY6J%2BkA7jbgz8VngYiMMIjOewDKL8i566gmCzuU8V66WicOmUnOaFT9U12dvvGwVAzPjdWF3NiRqYkYhKpOaIZgH9Fk9BpfhjCfTQB1WpKm7RyHo3enW4D9pEoBN&X-Amz-Signature=ba64b046104eecd0e01e3bfedd0e59c5e4d75607f457aa6510bf9f8978ef3e38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
