---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T35UXERO%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T223223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJIMEYCIQDWnrGzUkYYwKbVSP%2FvREJoz9AFAoGrmNzo0u1WLKgHZQIhALFHNVRH%2Fz9tHD0SPiBRVAOql8qOjbBaMVt6gnJ%2BcZJgKogECO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwJlSPqMrarOMVvkJYq3AOdrDjWcwA0WagJuRLBkgQ5Ytll1O%2BjTgFe6LShd9WChOaYXz2ETh1s7A8tJUkmXpQ9fLEGrv79aYzFiW%2B3d0mVKuiIABiBbV7woxa9XnMNVg2%2FT43olJzsd6AQP3kB6UeYB4egJk84%2B9e7yAgVGuxsSTC7TsqNGK1csfCjXg7dN%2B61b4xpOXSp0T8A4izCsIppcjqCMG%2B1jb1N0B8RgyL0O%2Bt%2FCXHGjPsPOK93q9plmg5nk5lzCBkvO7Moc854jRGkCrCEYdpRzvupTVSvqojfNLEAtzDeJShN5IOFUIns5HzzYhWW50J5UqXg05OX6KNkCNpLeZa86TwknY96%2Bi4EvSij46k1P3dKMDckhs5aILxGphVcn2YmWRFacsUGbRGq7783%2BfLh9r7LU1bEIqZWKVoz2DVi1D4TwqVp5msv75aWsMEpW56y%2FXusjE6zO7jP%2FkfupE7oudBUt%2Bu2YyrLpKt7bIhAm2NKhp9%2BWaYrQIBxcm%2FNdjfBq7FQDyQX9AM9DZ7QMyvXQJ6pNIoqefNu6oTi38CGVevJnEQyl%2BcAoRBDljWTAOB6bTxNUefWRnOUzyGfqStrlauTJYr7odgTjko8AHaWGrO9a2Wai0Wrs%2FW0cbA3hoavpdpBnTC52f7PBjqkATmJBYGSUw4e%2BNvdpM0sbhgJTdSpzlXOlL7BRcJxRpKxbUjY%2Fggm5K6vhRBeB2W9G8fKaTYuK0vy0%2FXA90dwlfqp8EXfUlLs5PXWC62yeFg5jSqWXvts92XfGZFJwc2IXwpmRc0tKb27O3fr%2BsVMuENs2gtleEsLF9ACYmqxL%2FjwyIZ1W7aVAktjWAdR0QkSUM5yvyqpNWxgPM%2Fgyk4wlgkeV9sB&X-Amz-Signature=4ba307d75beddaea0112b8b588f13c6a936d8f5d7c73eec41b33f85d70838cc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
