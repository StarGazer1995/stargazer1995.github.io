---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGLDVJKP%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T205124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJHMEUCIQCV6PDkR4O6KYb4HDfuGOtw816%2Br3%2FHnwgiZVa02ifNSQIgOGuEYG4BimUURL0esJNinFeyegIlEqBOQoTvGWaMspkqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBNquUB%2FZM5nXm8KvCrcA3HQ1x6rkVxBQCVJfGqxflclV4baqhUEiZ3MfBMQApK%2B1eiH1uLRhw8wo1HBThCnr9cgDuj6SFWMKNllQ1EtcENo7d6jzomLFMtFivyUQmCxaWaMYBn4mNAIozzxG4H2foE2VbgjebJOOp%2FvBwyfw9tpDh7rDL6PB1ygFQTsyj45%2BQHLOEjrQeVbROyc2ksHFqOUn2yszt7MY8PQMT7BFX%2BuSbjTJkqwB8%2F80bfuk1Wu%2BAS0TfRl7RsssX7ghSC5XfS99pbrDZAc5DzjIiRvNH%2FbOivZ29fuk04HtAYy2WlSEHq0UJQYH4jAVhjDCTsBzTtVs52RugjpyON%2B8P7c%2FTihhsX8w%2FSu6t0lttOqXYVrx4w3Q24vZJgv2WayQ33Q%2FPOJnUluDGbup3vS2fDiGfeTqgdEJIAm14w30Ydh86v2m6ds%2FmTRSskAf%2FRkEoZzxZjFhnIkpKyX7pd6BqIQ4rsjDSyiJKaOtGJiys2a9txmkzsp%2By5J8bNcItNgMN3bdG47QcH6ggLFrMbJb7m2ZSkY%2Ba7YTma0mj%2Bh31YHNlDttIYHQWkU3od500SVHdUu94wnAlXEABfVt5VG%2BtHV3uJRvvHbQiSIoMqBth7NluvNXLoj%2FgH3oPUdWioPMNL0mtIGOqUBKFNSDAIjsLPEJo76UkhmpJ9aFNcJyy8HQ6DtmMUFZVAWDdi2wTc6lCZ5vbaJdvtpczov2ecK4i14iPRTX7EhagHZXmnopu9yMzkVWXhz5AsjTFuip3N5yYXTOLEFP%2Bb1rC0uZObq7Gga9U658t3XKlbdfrA2AenjD2unxNXFl6%2BZe4C2uAeXwojvLeA%2BGdNuDYgVbDeInrdjRAC9GwSdp9JZzk0q&X-Amz-Signature=7228ca31c74bbbd49cb633e8bc50a5eae8f1d271cc1f7ec47b232ef92cb5fa78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
