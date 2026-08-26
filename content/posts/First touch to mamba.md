---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQX3MOO%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T003354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQC%2FCoUkLrJcbodhWPLHs1lMiN6rbsRrw5Ohc6qsi7UBCwIhAOaFgHbTgT3TujkG%2FiGJYQZNKDy%2BgXjEQgHVNGbr3Y73Kv8DCBEQABoMNjM3NDIzMTgzODA1IgxVjEAAWG74WGKxiPcq3APaIONKiDhMzHYXZu6z4D0v3YMe1KDbKjjEJ7gy1eADMEDdxWbhUZ09urXisoiCDjx%2BI8U3UONdaiaDprPwk5T9Ylebzv7c8EOBUjQcoh2l1yZORI%2FRTNwt5ogeBVKtWwhSjLZXx7%2B50HU271g4x7QWRTw7FgB6nBY2ZiDXiXw6N1nhMyS73p6fA83cr21Oltk3pg3gKY%2Bt9P9FGJUy7SVYlsgxMIX8jjz9%2Br1oojANQu4%2Fi%2BuBvddmcRyf0EXU%2B%2FT1LpiORDWVJRgDCXq4k9Mb%2F4Jhh7Rm%2B89dnnA%2FyoEP15eIsDZeAwJ4uBwxAIwnaYF0CV5KsmCXDwalXCh6j%2BmELhJrvWf0egScQNiwpgq6Valu2rFREHCGTYiIN1XH6yW0BNqVQBunIfwrP7wgUQdezt0KC045NEQs4rpq8LgNsbyDDBevc2YndUUBKpx2gvPOitLvu4tgs089fmlqGl6TH00DvSp1Hk0uL%2FNK%2BnHUdrnISjJndCA5WgKdguHGjk9lIOhGglOu0wMMoxDo33n4s5u0bLy5qCnL0ADsMkv%2FpNs9lFVL0YTy1TzQAv0XIspyhhd6fqfhIz9sAS4xUDrWDqdoBrAFuCZLPMqpp0CS5Z1bcuN5fy6yv9KH1jCw1rjUBjqkAVTDPK8%2BkZJ%2BoHMj1Ue8%2Bkbl2MItICpQBd%2FLYkG9kYXN1a2Hf%2FMHWn1CBQZh52V6UMm2tfD2vH5oeAYQAinhjPLxNdE5BNIxUsXAV1%2B9MiJwCRSNNtHVFme2W6YLp%2Bf05evEHPZCsqV2Oh6lakatbWcmS709D4tvRsZp%2Bri7iyHj0OLcKkkTymtzmHyD%2FTAU%2BQUK8ZWXumnCu0dMOTGyKBPcsmde&X-Amz-Signature=38fe0d37f8b362b450e86993867dc89938485aa57c88aa1c4b781230525ab100&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
