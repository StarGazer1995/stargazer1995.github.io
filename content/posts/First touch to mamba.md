---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN6VF2XY%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T051830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFnbfCXoVAqd2NgLHvD8EtaDZiJUj%2FAcFttt6G95pwnGAiBlqlbYl4bidP1gZC3%2BydZrQnTxO8z1h0f8jzzcBh4ixyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM73uLLip6J1SxxJZDKtwDkd1KXRzEjH31PMNX%2FF3%2FL2wo%2F4pYrYSAJxnZdTs8QtXnES3np2KqghGxEFHWQhW7yUKqv5NrxfnaKdBU8MogjOkfA%2FEX4P8P4n1zu9fyHf04Osy7vBOqaCaM95H0xMEYBwccDtgTbrensWD9xHRw0KoT1SItty4itEaIxQ9MZBFowhN7m2LmxdKAKRAufip3OEhQ%2BRYpav3lF%2BMENmXeVcKM28Hp%2By9lg29Z14WsIxoj%2BQ4ICNI7kah1p7IZUOnyQva86QDwttAGbr0mFYbzwzfUE7FAK2FsC3tZq8gm9lZAolOl78EcalO%2BdwFy7fIHdvI6e1O4BQyyHY2N8%2BH%2Fl6xisycz%2Fhd%2Fpi2kGzNjYL8%2FsVDraWHS6mU4MxzRCr3eRYSTgbOZM0coY4W6L3zIrFlPopkwCHQtc5iCzHd3riKPjgQL%2FGJk8hDZvF7Pz5f3JLrFzK%2Bq02n1dUg3miMh7KDcyPzm5LtfWfGd0hRziGW8TCHB2xxfZKdzOXmiyatCz6EGovFq%2F2PCS5pvMNYOOdDfq9sbMW1ISiFuuZNqjnqXACXcIKGWegKsC7Ens5hcCcqnH1ygvsQSEIafQpu16L%2FJmIpttXTDesb6%2BOmCH7Rh2SvB5CWQiLVbd3Aw%2FeC10wY6pgEcyb4k8MaHWJPXUvLmJ59Q3wwdMnpge%2BNfum%2BfER4KPUm5QaaPn%2FyRA0OmE1LVjHAY%2BvmmYo2kPacFK6H4zMWmLYhY5iZBLZlb%2BoROogNG4HJOV019h4E0%2F5KlbmYmst4czvw0JbTwaLEC%2BhHluHU8jOPLSTy6IkDsLG%2F0RjzaAO7mvk97MYYNI%2Bie%2FFODNpLM6aaH6WGsSWvYGol06Ih2fS04zSQP&X-Amz-Signature=7c087be6f997d054a48c71d276cb4cd6b90d8e8d0bd9078e495f9a199255b48f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
