---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VTHGMAM%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T161528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF8Qlm7TUKERzDbFXmo6BAptFQu21ac7rrGKUY0yMymDAiASsG7OsVFqCFInae9pjXKFukOLTifToeb5RNOwM0W%2FBSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIMXT1sWBceI4pIVcq9KtwDOiinFRtloeNoy5NTGTP%2B7e3gmwJ%2B4FbxNxi46h8Px651FYIHwMY3RxUzUstuENnKojfvFdN2QXXyqrjgUkbWCPTaBZdpC9dtuqU9KZfmupSO%2Br%2BAsmpbQzbkvO%2FDENiBSGNcvjX%2FdwIYAcvryLnoBtYXVjZZkfyfNXwkTFpNeUCvHBC8%2Fj3L0y1tSwVOE3Pku6AcYDS87L1Rh6HV8JsrhjcoWLTh37tLnu%2FfvTjM%2BHtNINxuO4wjo1atBBUgosXaV5vwSqIHlD9MTg27kWhs6zZ4uboBYYtKEDI9Fz4eZ3BnrUGkahdCrjMBfgNeuG77Gf7G7fjtZRxdnQdEw9o7rX%2BoPbcjFJ9%2FJmlG9aMpvmLKP9S%2BWJcNKwLvgekiA6NZS%2BRAZ6FwSi6aNcXryd5NhDKuFcTPl58%2BNgz2oyb4PHc%2FWT6OjwI99uv0z3LaPqSgSNGCevR6ffogHdMMy3vTNf21%2B7AQyMMbNRR63gDguX6DkMLOjCeDkuZp5iSen20K%2FQmgBfvJK2jwxtpSNOphJbBcWpnV6G4heIzO28UT6olFbxG%2FJY24fad%2B2GBFWH4OzLfldc3LFNuXWkblUelZvm0qEZM%2F2A1WKevpH5G5X18NajdH7ZyCED1yqcow99%2FR0AY6pgHVHXgsJz%2BFTd1pxr%2BmUtPmQgiS%2F4RxMH6h%2FJumVJPhBsdljWA19fMmjh2Zr7N1mPo%2BGnIqyZHKJ33xLc4DeawxNnZ0bL6rSVvpF046OBZhQCg2%2Bcn5ZsRGbcxQ9yepooEPBlxPs5MdDV3uKtJMS8X1wMlH%2F0AezBdox%2B7M3s9q0CoW6C9mF5ax0F4%2B1hKpc0kLWNMsJYq2e5A7MO8qIycpwObA7jQD&X-Amz-Signature=15699abfe54d0199e073ce2b4f3eeec35bae97049f3c7d3a93edac13bc2f22a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
