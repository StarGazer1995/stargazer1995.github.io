---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XYDLJHI%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T144334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJGMEQCIHS9jw%2FF9jgh869H1hjTePK%2Bm0UnHF1fiLtNL6nXlXP8AiApHMJbHQN2bRXmZBmvlwrB0i05wMkiKULHoR%2BMkDXwriqIBAjo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOCMnx6%2BN3zumljL3KtwDtjIIXngwqIdaatPpuoE4IhNqs9C0eVW7wJbT9u9249vahWe7NDYD2aUsn%2BIRVxgbm9BBcPphvv3a8sS4rs0SuTZIbDNwpd4P5vS1tsQiAb5fmX9thET3FeSGpBePlXMzNqYV0NoqCiDjLOMIxB%2F%2FCuT1v8xuiw6SJGLWGSE7qdDepW0WPsU1vtFI1t%2Bp9Ecz2z8akC3FLGBSOV7sIrPwxVS%2BZYsGuX5HlnZpYLEkB28bbBuyjKGbCfBn%2BcLuNIK1vja%2BQx4vU61k8ZYpbbGsIft4ixe4wc%2FqiGM5oYDYrMJFFUiG5JUhctWELANjhh%2BDy3N0yYpn09elVlFZhO9YbQH6tCTQWtu2N84q%2F7EensthTTip7yUiHkM2QLUe%2BMGlI6tveHHKLOnvspZaDh7pZg3Rm2rO%2FkS7Idu%2Fa9QtV1LTZOlLhiv2OmwwjCzN26f4cbhUS7%2B458f%2F7piKjHpbMQfgsN05%2BF8TKUvVBh0nXv09j7KYHtoO2hzUXghZYkcFqSek4V%2BhgnsfMp5PBGzFojvLbqB95aoPngpcgGGzX7VAxGXkx0cKje6MRI7Xqmh8bHdItG3IV8KN4FpWrw5xsKinO1IaXblvInp8VwogIT7w%2F4uC%2Bsv6F6jgwjIw3Y39zwY6pgGgHGsg%2FyRRhyV6J62%2BQG21CPzAiSEitjJSogIMv5t8pyhjIfM%2FFuX1rTJeTogKrizkUqhQDsqp7Wr%2BB5iZJF3t6eYepq0VX45VJV0sYajEIFtwi%2BXnjrcH80WR4aHiOvYg6GnoQttO2Ruj318USGiL04qBPQ8QxK%2BNuPSP3CAu%2Fx3CXi3koT3NkJgvqfqHtrW9uQSSasJ77ie%2FhEckxig%2FG5LMJm%2FP&X-Amz-Signature=e819e4e9cda28101ada2915aae26f5ecb0e59bedbfaeea773d9f4f1acb3ed56e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
