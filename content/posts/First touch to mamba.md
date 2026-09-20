---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6BWTPZ2%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T235131Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCK5zX%2Biw9NlexzxEkBioFzBFiXNDGrlrG9jT4LCR3TgIhANZxxRN9DHJgo%2FPAtt9BR5zEHm4Pc9TznR2YcJOH7LYfKv8DCH8QABoMNjM3NDIzMTgzODA1Igyj9%2F0XVY0Ur5TxAosq3AN4fJLoecNmGZo2fRpOur%2FPOCfKISIW4zoIY3Rx7pWvUz2MXZPeCAqEr%2BwednnrivBMOPEt%2BOhWEXgnUY78wT6Zarj2%2B61s8FfDVvuI3OtQY2C84Hp0r9s5lTbVEjWOCJYzvEcIUD1LWVi4WrTHDLYOsJivJTD1g1ZO6hWI0q4K4c7dC3Ti90QqlHOnYTIj01Tj827DQNDUkzU1Fd64AyHIp17qKUS7LxdMZ35BUS%2BB4v0Vj4GZF47H8fZgahleuqMdZmr5gDfK%2FZzGbHRq4u5GRKeylOGutgtmHRC9hJDdgOyIz3woH91BrbmSwgWpTu7rVN9gMKfRjTzQEb7HeTWmIGaYE7DBga%2BbdETRQXtLzJwd8CtCyRgL5%2FT26EaUAPd8OrqgmMAt7Ne%2B1A8qri5BKoD5HnFrjO9qz24cQi9U3%2B8n5gCjOZBqL0tQRDKNW%2BOAra%2BtxVdJ%2BoEoNJXPn%2By4nw3I9t4OJGL5JXiAttKL%2FhD1ri9V6xBVdYhORGasEkJH%2Fv6YiO4m%2BuSFWs4tFoBn0vCeOhsjb1hNXQUPi3ixPw6QbOYZd3X%2FYYaG0wwOOGWJrefUJvg01flehz15EZ%2B9miwF8aDetk01q5pknRP9%2FxlVzSlkfekGF5r5BzCwqcHVBjqkAZS18erH%2Br20m9k1hPqmj7L0yB2Rgh6WrnPKBF77MimxJZKijtHkWkJfPyNm5zFkx41%2FxyoknF2lbFj2YFGzN2ggxW8RDudaakjD%2F0xbfQdFxgbLLA9HwFVYkgGSfTmBROBRVtUYziRW8mwEY532MocCBsNhbjVyC9OjkJFhm0NDC3RmT18hktQSGui24ZFHW2wNGC0EJV7AUvnslosmYKtWwPSE&X-Amz-Signature=56cd0d1aed1ef326ad6472973ebae7560de4b0e01120aa4026ffc874a3f84306&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
