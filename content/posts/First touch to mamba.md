---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCCZ2MOC%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T020301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLsGkozj4171FSeLvMzMan8r%2BkikhY5bYlAk7zgugVUAIhANrc6J6TbljI33x3kBLSseExQcdtBuicKkxfjHW0xOjvKv8DCHMQABoMNjM3NDIzMTgzODA1IgwbpkroajASvhPsWi0q3ANyjCz83SByvKRrml3mfLnrz71QI8O%2FDGS3ZUha%2BR2NfspEAVxos46j78UOipzPTcCrfetmk6LhDz7cLro3QQS2uIYVcHv%2BigzBKN9xtSzxA1yjq7j%2Fj%2BMjoIykSS177wc%2BSsAQLQQc%2FdawtJT%2FDRd758bWSgd9hYHmn7xFPvTSQ9%2FIngBLfokm7pzlUf33naDQkjwpFXhKxHx4dkLza4OHQ9SnIOYHVTI570ufBnLBixY1F3DQeexZJk0z7zRFaBJaUXGeZlukwVAQlMMqKBWSqjIdM4izKgypDwH8peHLMMaxk7amegO5opOkoqVyHWv0WUvRd7EXGmjrp5H2oaWJju86it0a7e9uoFJQlGXNbfM2n4CnDSzuFK%2B9SN8UEncBavoy91kmEgBQ6Qa21YHiC4EkUR5ok2X2weBPfm6k9qUJP31s1RjvCUQdqfBhh1ojo2IcDcum0lVTjQXvPZjn4LVYfE8tXbybkNkywN4Y4YdnGUiWWtuacJGKlxlu72BWICCmtMfBnqtADj0aGOt55kt%2B3ikirMcCz%2FcI6yLbAf89JZsO6J%2FUlO8%2BH0gWhl7ARfjIvCW8DNhU9hcjlXgpaDhpOWvCkYhaZ%2FEDuwcT7cFCk7XsA%2FcaubSJjDChm87UBjqkAQaHR2X8Tk6CsKmY5omYD2NiDBeavKlHqk4FjfGCknvJbuUy0AnqOmK2C3tH%2BMtdESt57TnP5h5jS7csAAYl0qiAdtalrXl5m2DQuPwivd2ZKzPRJ0tRWfgvmxQSsZ0yfu5coMbARgMprjCtBAw5PJltS%2FuodlJ1cW6mZETfszSvVW9DW%2FvBSn6VPz87FIDC0Ds4zDt7aV3JQusqDPxfo4mRGmmM&X-Amz-Signature=e9af0cfafff07f169ba6eedd647bbe34d841755974fe8886f0fbd599333e905f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
