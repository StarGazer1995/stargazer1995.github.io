---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVKIXIXD%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T195955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJHMEUCIQC0y%2FLzF5%2BcVOgmMtly0NwHSLvyR9c1mLWILGgyqkXVvwIgfcu7lluB7Ofr5ZdZlEo9jInqQmDgyxne8Lg1zUqVnnQqiAQI%2Ff%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJfzASYGkCv9MEzGyircA%2FfDYouNMFIDklJVKWpJ8MzBVHxreZs9wzTOAh9%2F0DWwFdeJu%2FH7yjKJAMqg02Kwu9ph5G3ynDJIzXdm7C4XhuNXLdTEa1sMx4j6rgBbWmWcp7jIz2OY4y4MT%2BZoPULAxPyEQ8iLrzT0G%2F1H52NR4zBRiyJZLwKqD9yENGQRZ4r%2FXuHgtA0zAEif66P71fmx0y5yuiSxG6q6L%2FjWYOjb8TILptkkUWHhC6E2PHQ1SvL8cO5AB%2BXB6%2BZCd%2FQ0%2B1VCwDcToc7zVff5ySs78Hi7laaeatefB6O6ujvFj%2Bbo8%2FgaKXh1p20zhK1a4fieHFJhdSbbpJSneWIE73sjc3p2%2BxZ6rPInMbagv6nKNdC%2Fjd0xeu1HrNaC01lYbwG2AQMJ4sYrVAUKkQKGi6EyyIuekuseM%2B8VUlOcd0m1qbMhTsGKcAPHeXp%2BaLdqg5WUV3uMeuNSDCU2ba2pEZ%2FC%2FSUc2R1SZEkfyhozzzlDwAUtW%2Fbw4ZdYua3b2o1WCuY9FmK21MUMTXF3kauNV%2FjUJ3YCZSE8rD%2B8%2FpdCi1hjnrQAll7Men9K9JDtKeXrlegt%2FeezVwpROHVrqDTDCxtTtMJZ67X9S8bDh3IJqwyl%2BQXDXy%2FRSx5xsywXbWbEfrNXMNq97NQGOqUBD45nV4T0%2FsRfF4L17t34ymKGzYqm%2FuNHF3xcdKxr1Z4Zlsh1c5POM2h0KI%2B9VoNP3G0DwClTxiXdP7m6%2FPSJmXd8U4ozdKUqBogaU3yBGF0C9Z9ZubaDKXM7W8eqWpctGcn2blCONUEBh5VDRS29NopM4S6R15%2FeOu8pNBCwjO%2F0A00YoFDc6TxS1jnqXTYROAdHO2C8plxWPyQda2h%2FXgVdQITp&X-Amz-Signature=1226563d3275357e525aa3410bf3c75e83e8cb8e0ab8af64d48b0baa7155eaa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
