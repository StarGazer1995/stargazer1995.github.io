---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC7MIXVF%2F20260619%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260619T210037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpaiifNU700ol6O5TEfzGxo1mE983thRCXj44pekfiVQIhAMpvnLFwIVhyKI3Zf3OGmP7bi1e6fCWg3sls1%2Fv%2BMCzFKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4qkL70Vm9juyRXfYq3ANhlwf%2BJ%2FpkyHO3QkNTHZ%2Fo0E93BJum3nOTQ2ZsmFB8cw5g8L1fiPY7R7RbTQcI2E%2BfNJvyCXdjIEbDLg9%2FeHr02NCHs3BpL1h2GDTq3zOHJ9Gb5bK6RsQbMQcXccE9Ty5VcQe35EZ7p63D%2BypPt8v5nQwNxa4RECPE3WOcrwgeExAiNcry8Q1tHq5sFU8y11CfNfVRsbZbXa63sKZnr7dH4n0YogFS94MZqfvrLBeTqT03%2FT9mRp%2FmDagi%2FTjEuKdBC5JXvYqZ4fIzg1JHV8BqpOjWeeG6o0YVmAzYkgn1CHPj6%2BvGP0KMWwDfwcPR%2BwhM6hEf3qZoT%2FymmNB70dLy6RPmBmdIIa2sXuH%2FaYEpBcipG5HdfjbsvjuaiXKcv9Ku1LPB8q9ae48lfU4evJStltRKsV1R3fCtqEjaXXqAAnIAMO%2BXtsbNu4BfCB1dKCtfJxSDrd08aeuhqL95mFmIDvQjv6keAjSuMJzJgBAZA%2BC8a9j0QLULMvhOnKvxBPFIvwG1o49OjhlDbTSZJuPrlQYsA2aXvQHhpbyX%2BJBj7MWMCFPdVUo0V8meJAlsLCcdT1y5yLiKF94BnKaSq3lZapxx80USduCLBlP0RITzYi5ucDo3rpSBTKum%2BTDovtbRBjqkAfx7C9fxzHE73yPIg5tQbO9Vwyxt%2F7zY4H1xxbK6BfGssbRTyz5S4lr7y8EwMCEtSVlf35JKj%2F7%2FJ2kP8Rb%2FHmWosUstJ2DcafpZPklzWFi2MOJl3gL%2FDCFy%2FhsKNSOjgU5lmlfwgO%2B9TIEtYqVLuTnulhUlrQAKKEQN0UeCcA0YprQUBYrorCI1dq8fe2W46g4rNVHq7pUiULZYRRMhWu2cbpDq&X-Amz-Signature=6c8679713aedce9787345a13e734323616f0826992201301de14243ff02c95a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
