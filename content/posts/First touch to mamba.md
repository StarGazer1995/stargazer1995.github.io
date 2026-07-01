---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBOB5LMI%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T021003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQCEIiN4AUopSGKW8%2FwS52szBcHnBqSR0DlwhNTj7vNgwgIgZs%2F1ixwyCZqEkK30eT%2Bec0HEPOL8sgb3ATOEOprHQO4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJOkydXpKLEFstcGZCrcA1qrKUm9mi%2F4r5CWDjcwgtCEjEM%2Bl1HAL5i0QolEBcOWPCETZr4iGHflWnRjYJPnW5gwxUdYRP9wfxlpDpGepO5z3UBkGHpVXQk88KiRaOMNUC9yi3e3JrdeEox01I7TOnXzzqREqAexuunl9VvfMtrTSM5gIACRgQMQ19ljo33902GS8VXxDoXPErJ%2FGzfSaDiXR8kHnFkEGnCaSQiWqZduXedW0zmi1TQvz58LHVZ13eACXZvUpMNLaUKoCujEDKxox4r8Oun78AC4mnEADkA2XNmRHqZXKgJxcvpE%2BWQYjkIfXlfHGq4JBzaxcY9VMARK3LFeAEZQzyst6Exitjd7nnbghhzUuuv4DoPb9kaQ3UgF6KbEjmDPq7D5wd0wGYhUiKsdN7rI0%2B5ipiigera3ygSTbDJKIPCMph96xTkFLLiX7KOwzeG0T21oz%2FgqLXasA78o4WG1hBBFUIOo096VOvjDR3vv%2BDo6H8VijEd8PStzZa3P9EbqhXjSnvi7QAPGFDhsqxOzzRrxf5wwjktLl%2BSovBcxwO8LEDrOj8EpFZS3rQ55lb%2Fv4AWLFSfB%2BXm0631BMsM931yGBwSdnEcrmGv2q1c5vgY9BTod5nQq69RK1ldE7C6xsgVwMOufkdIGOqUB0ZR2%2BoEIbpTkYs4qZJ80OKJbMJLXTBkL0WSicK3B6D0a9%2BfIzB85%2B7bg%2FmdwotRuJTBmBh4eGQ%2FFf2hgIRTc54cxjlDq7OGavXraWmX74VP4PW5V3mofvjxRsW%2FVBqcUif%2BOdMpTOUeZ6mnU%2BJtuyf5ww8Sq8nWsDW9mJQSXPgv%2BfvaO9hizJs33El7DPmTZsQqD8vhETTm7gCs%2F08KkmkHqiEr1&X-Amz-Signature=d9ef8c85b064cefe883bdbe39bce2242c123a05c3d22bfe584554192d6430a1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
