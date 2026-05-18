---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWMRSTED%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T020325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMlZy0YSLqJNlrnaR%2BVpChmYFyYJscIprm0%2B4KySGX4wIhAPDwDEt25rKBFhnjfj6xg32LM3sxY5WYvrBSv0dckpdnKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwkhnODs7CRGAtH%2BXYq3AO2FNP19sGujiRFSZ%2B3na43JW%2BnP%2Fqea37cHqPJ7Im%2BiZwB%2By22BwqhIa2gD9SSfmJ4KLBDTWJDlLSBH863SsiK2Lt0z%2FKiG6MjtifyJeGGk7dngjgTEjfhD6lrwDf3DVHgSiI0Zd9deiJLudyA6P63OJHrp7jyATmH885n1%2BWntZcOjCLsGzxFHvEuq9KfJ9nGAcz4tb4VVZh1UBFQEbb3BjfRJExw8r%2BNINe05Yy%2Fji7wDafCTws4sp%2BdrzejZpfL5vDzJT6XYL%2FHOKmPCKOxnSkrW5Sdgt7J8M5X9XClxAppa7ib%2FkB8LXUyHmYEj%2FkqarUci5PNYJjbYslkjsdCBsvuI00QTD2oOpvYwsKz2u6Ruex9xGd9SpFBHgUzaaJv9eUDu5CyIM724M0JbZaA9vK74IWzJZP6f5fjkZ%2BeC9T84%2Bi2LbSQbRlXgMsQwMv18x1X%2FhqSI4HVfotYzEaL%2FyelShd9oOA8pKuy99aEkuZCfxobEiUiNTlX15c4wwririHkBvssIgkPnf1SngcH%2Fey1w8nsH2hIG244Ap7hWKKplwCEbF4iV1znpTlXyg7MJR3RcIJxKD3A0Q2dQMe5pYSBptAGWWDj%2Bt65H49%2F4sQ2KE6Bb5VqF0XjZzD6qanQBjqkAZsXfRFMCeRff%2F9IO3usZZi81Xof1p5Cx%2BUEmHs%2FIbqM42BxQe9sur8clL5qjL1aTa%2Ff%2FVs78%2BHvSOLa8%2BPbg9K04kmWCFPQL%2F5Eb0nwJD7l8h26caJaAjWJybpE4Hef9HsRm8%2BGwnUmNP%2BwQ5thQhpd16OHeQGaDZuSkdaFEP1Xk5%2Fdn%2BxQurosGB1Ikjv%2BZazTXtapxWRp4EiJUdA%2BIVVQVBq%2B&X-Amz-Signature=36bc9d23e8b6f6c2af9a5cacce3bcf811c1ba7f47d7435c86579bef29f122849&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
