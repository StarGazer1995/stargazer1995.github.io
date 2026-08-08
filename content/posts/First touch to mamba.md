---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4OEZYGZ%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T182043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFt5DOCs6fgx1IUU%2BV4dGlcHKUjzWo2ShjpBEgHVdPPgIhAIcTNvGy1pYYU8ACYsaOpHVV7QZaeu0SVwzkqzOySSv1Kv8DCHMQABoMNjM3NDIzMTgzODA1IgybkCw2W57%2FydKAibwq3AN6OBrVxop%2FTkfr1sGvA4Di7ZWHvCTXe2v3qRw8g8uMOOxpzlB2M84QtIIzkllUTNXdLFjj5ZLj2SU9Rw75F5aTRR%2Bl3DWVvoOwcOw5JEIN2pMQcBMPKWr31ChuILilSiLJllQJb1BeT1qJXAB6l%2BzH3ZTbWI%2BnWPz4WGS2i3Si9vFQ9TDDOgeoz2OtNRFn7nVKPafR1efJnqDphfkVXivipA9kPZaPvx1VFlvLwLnmrEOMOkNKxeLcnN%2FHyhcb4HyqmRFMxSobZluHA9032pAJCXMA%2B0Mw%2B4dRHlIxweHfH3mEWHNl2Z7cVPkvEAJvld1Dy%2Bh7ygxM4HCbsABL0g0S9Dnoo07hF2j0tbmcQXOTmVQ6FJ3HXOXBMykcyyFBKHu6a2ZFOUR0WS1OCQNIQ%2Bh%2BZjSJzn6F0hNDNb7%2Baqp76sON2VzBmtmeBDgjs9gEdjlyh1hFzCNVoNquiAmPCfoJEzmV0HxPSW7O8O%2B3q1mg5NIKKG6QzE25RsKaX8oguqMqjdEsDpYHDGIven0kYVQQYxTZL%2FVcxeZqrEI153xUchBw2IzAT1Y1rDPA1vC1chZMmG3fABFWhgH6nfGeSAevfrpjqFn0JLPsp1YjuQaF189E8o5SI0%2Fv9zkQFjDJ0t3TBjqkAe1ZNSFijOI3ZLWzJeDG%2ByFLO%2BcAZYwa5xNOcZWHrNYLzdT%2FUzlzsxZ%2FDgj1D8HlYAEFhN2tb8t1qrQ5kZKvzIBh9HuyuFjEhg16t6R8ZRYtCdG%2FUfUItbHIQ7hpoKebGj7mI958ebzwiqSiSZKvxyeN2itoaEPF1Ze06mHBpbj%2BRn1FZ1QBO2AQHi%2BoBXmpSdikB36ASOH29CUzPOn8War0bY0v&X-Amz-Signature=d5a57858e194e7a02a4ee31b7c7d45133fa75fb79f6ba1a7449b14e17bf86375&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
