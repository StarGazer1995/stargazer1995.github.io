---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFHJYKTQ%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T063843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHHSGivyTL2BQ%2B6a%2FrLLIWpqzXtjchg4eqFs2nUk%2FxydAiEAwn8zxeT97cH7E5J4Zvaqcu7aTkIZuSzKWIzVF5rhZv4qiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDRZUwTHFOm0xGQLkyrcAzSUeDRLB7T8HJFm2LZQbhjUrYsYYyUEBzaRNxSKeCqT3Zz3Rww5VHYWo%2F69zNJsULql70g%2FDd1LMQMG%2Fs6zqWKSS7L6wKECRAKqD1ylkNc3O3YXlzH8ZFFW8130ctQhlAQPDw7xbxqcNVQWcRox%2BzwGK8ONxPdc%2FaYHK9qCveP8TLVu2imIsl1%2FD9LmmflZTsUsaVITTeXKYob8UjlSmAzXGyEX1TqrFRiDxbceIPaT%2BnMaiFEoowsp1jJ5AV2lhrDsCY16eujEWxitxxTzq06UvqbsaljUGM2m8S6kPC7dB%2Fnvk3h9C92XUYzDBzp%2FXg7wXvPMyLFCI4t2%2F9gff7IGeC6BTxXeFgKNNJ8y%2FdHvTtmHnxHSkwOCdCH%2FHq6k33gLoBMnaJTWANkzqQMgSKfPDSXwo7cdX3Jd8OZSblc%2FQOAfcAGFGh54vdHhwMQGmJK3GA2foEv%2BzteyVLIh2rLeffIFwll2coJIF2ZV0KSGBIaSrSacVRvHJFAgHk3hf1swrzoO368v7HzWtyX%2B6msMvp6KEg5YKLwtzakXJFHeRsVpk6oUSx5ERp5y1ri8Q6RJk%2BywRNzIKgCNen%2BfVFEJusv6%2B3AEnPRR%2FauQnjZQofHL0sMI4Lq%2F6uo1MIe0k9UGOqUByqpKQH2sdUrzIQpZiRFwVuPxYj2IUwVAKssdsrEPp%2BUtXitX8AswvYFk7mWuE1ye8EjazDUcARL8lbXuxS6LHmZX3l3TurcDLbaWoy%2BKp0PjjkFRiAmmbDu5HWns6dtdqkRcJuWj4LKnvQ8xJ%2FM4HfnqDBkHwdYOqEHF5k1Qzy%2FEl3kpXLf8OKO0aSSvLT0MEzpPTvUPJHMxejx8A0ORqK4pTCKq&X-Amz-Signature=990180139f3242eae2b7a63211afb37a37e92c48ef0b87ffea29664ad90a81ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
