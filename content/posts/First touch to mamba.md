---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664F622LUQ%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T203944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIHxpn8%2F1mhIJWd%2FJodLBg%2B3rLkVKNG3n9YuCTFYmh6DXAiEA7uitjHyMi7mNtEGzPRq2pjlwJl9mniiRED8WC2b6IgYq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDPt2OEYt7DOoyz2DrircA66kDEIerDtB06yyCRi6AJEqAEcQeOvOTx7EIalRihzoZ5nWufBuctzQAuGNg4GxLMGSWV%2FTAtGQOxpLeICLcWgwFfKHHsnZjQCEKBTP6JEiQ%2Bhv5jnn8zPOVbLcZcnlTDQbz0AuvQ2YdBF9IJ2glLTNG4LTMk5g8aTGsvdf%2Bk973wgqs8Xc7679ERuHXFqhZWDCt6Wb6HvCJsfj6Vrbeh1dxW9Ftg1qsfTPL8XDYy8MLq7LI8V4q5tOGW0r1X%2FXwX%2FH%2BZ95z33HV%2FQjiJOest5anO2Ymzb0BAnqB3B6Io7NDz4EwZYqpORMy08GAYK%2FRK7q6RxYv0aXgmW0rSNZGgsqT0AoiAY9Lhhhsm85wKUs3WDrKTaDzkO3ETprnxLbWkBaJHJL%2FuohOcOvXHlvkB5MqGznDQewKsHji1sat9%2Bfq%2BOkRiO3VdyAGNns2Y0VwZAv3Qwo4BuzFT4MCf7tp5I83s%2BDjUY3hOxGMupcy0wjbiQD5JgN4imfchXlbvOM79Wb5tTgB%2BkzatLLl03%2FoO5jHpXe6Zoc2B1TkKvp8%2Fk3RJradQcB7BGrcOGlKBVZh50roYBTXQoBjiCAIhX362H%2FqqkbdpiA2q1jN9yNYhvhermoSwO%2BUYZeynLVMKuNlNMGOqUBZi8IpVCsx%2BSW8VnkCAHqXQv1zZr4J81kYuyJvWo525J1oRKdRUWC6g28to2ZpFOb4iQZVrNQUPBd2iNcCL4L7Gu4wkzp3C7ssbtsL5V0uDxXPEy8BaO7sEgrDH3gfQPH%2Bpcbew7zpECJ6F%2F9ynRE2l0EATRGJ9q25TAPiD%2FVkVhIIKHnmxXFdhkB3TG8pfg%2FgwIAho8sZOtYhysE3JxNVGSrhP%2BH&X-Amz-Signature=49cbd4611da4c711c60662ab2a2cdf1252c01e4fa86fde6d20617949d7d647d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
